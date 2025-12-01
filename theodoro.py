from pypdf import PdfReader
import locale
import re
import sqlalchemy
from datetime import date
from datetime import date, datetime
from sqlalchemy import select
from sqlalchemy.orm import Session
import difflib
import os
from pathlib import Path
import sys
from orms import Base, Councilour, Attendence

def get_councilour_name(name: str, councilours: list):
    names = [c.name for c in councilours]
    match = difflib.get_close_matches(name, names, n=1, cutoff=0.7)
    if match:
        return next(c for c in councilours if c.name == match[0])
    return None

def get_attendence_status_from_scrapped_str(text: str):
    return re.search(r"\b(PRESENTE|Ausente|Justificado)\b", text, re.IGNORECASE).group()

def get_name_from_scrapped_str(text: str):
    return re.sub(r"\b(PRESENTE|Ausente|Justificado)\b", "", text, re.IGNORECASE).strip()

MONTHS = {
    "Janeiro": 1, "Fevereiro": 2, "Março": 3, "Abril": 4, "Maio": 5, "Junho": 6,
    "Julho": 7, "Agosto": 8, "Setembro": 9, "Outubro": 10, "Novembro": 11, "Dezembro": 12
}

def add_attendence(client: sqlalchemy.Engine, attendences: list[Attendence], text: list[str]):
    session_date_regex = r"(\d{2}) de ([A-Za-z]+) de (\d{4})"
    session_date: date

    councilours = get_all_councilours(client)

    for i in text:
        match = re.search(session_date_regex, i)
        if match: # will always hit this condition on the first iteration
            day = int(match.group(1))
            month_name = match.group(2).capitalize()
            year = int(match.group(3))

            month_number = MONTHS.get(month_name)

            if not month_number:
                raise Exception("Ocorreu um erro ao obter o mês de referência. Provavelmente será necessário ajustar o regex.")

            session_date = date(year, month_number, day)

            continue
        if any(x in i for x in ['PRESENTE', 'Ausente', 'Justificado']):
            councilour = get_councilour_name(get_name_from_scrapped_str(i), councilours)

            if (councilour is None):
                print(f'O vereador {get_name_from_scrapped_str(i)} participou da reunião de {session_date}, mas ele não foi encontrado '
                      'na base de dados do paecirco.org.')
                continue

            attendences.append(Attendence(
                month=session_date,
                status=get_attendence_status_from_scrapped_str(i),
                councilor_id=councilour.id
            ))

def get_all_councilours(client: sqlalchemy.Engine):
    with Session(client) as session:
        stmt = sqlalchemy.select(Councilour)
        return session.scalars(stmt).all()

def throw_exception_if_current_month_already_executed(client: sqlalchemy.Engine, execution_date: date):
    with Session(client) as session:
        stmt = (
            select(Attendence)
            .where(Attendence.month == execution_date)
        )

        has_any = session.scalars(stmt).all()

        if has_any:
            print(f'Parece que a data {execution_date.strftime("%d/%m/%Y")} já foi executada na base. Programa encerrado.')
            sys.exit(0)

def get_councilour_by_name(client: sqlalchemy.Engine, name: str):
    with Session(client) as session:
            stmt = sqlalchemy.select(Councilour).where(Councilour.name == name)
            return session.scalars(stmt).first()

def get_last_attendence_pdf_full_path():
    path = os.getenv("paoecirco.org_attendences_folder")

    attendences_files = [f for f in Path(path).glob("*.pdf") if f.stem.isdigit()]

    if attendences_files:
        latest_attendence_pdf = max(attendences_files, key=lambda f: int(f.stem))
        return latest_attendence_pdf
    else:
        print(f"Nenhum arquivo PDF encontrado em {path}. Os arquivos de presença precisam ser inseridos nessa pasta.")
        raise Exception()

locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')

client = sqlalchemy.create_engine(
    "postgresql+psycopg2://postgres:postgres@localhost:5432/paoecirco.org",
    echo=True
)

Base.metadata.create_all(client)

today = date.today()

throw_exception_if_current_month_already_executed(client, today)

path = get_last_attendence_pdf_full_path()
last_month = f"{today.month - 1}" 

print(f"O arquivo {path} será processado, ele deve representar o mês {last_month}. Se isso estiver correto, clique qualquer tecla para continuar.")
input()

print(f"\nIniciando a raspagem do relatório de presenças em {last_month}.")

reader = PdfReader(path)
page = reader.pages[0]
text = page.extract_text().splitlines()

attendences = []

for i in range(len(reader.pages)):
    page = reader.pages[i]
    text = page.extract_text().splitlines()
    add_attendence(client, attendences, text)

try:
    with Session(client) as session:
        print('Iniciando inserção das presenças/ausências das reuniões.')
        session.add_all(attendences)
        session.commit()
        print('Inserção das presenças/ausências das reuniões concluída.')
except:
    print('TODO')