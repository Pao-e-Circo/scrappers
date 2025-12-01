from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
import sqlalchemy
from datetime import date
from decimal import Decimal

class Base(DeclarativeBase):
    pass

class Councilour(Base):
    __tablename__ = "councilours"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(sqlalchemy.String, nullable=False)
    phone: Mapped[str] = mapped_column(sqlalchemy.String, nullable=True)
    email: Mapped[str] = mapped_column(sqlalchemy.String, nullable=True)
    photo_url: Mapped[str] = mapped_column(sqlalchemy.String, nullable=False)
    party: Mapped[str] = mapped_column(sqlalchemy.String, nullable=False)

    attendances: Mapped[list["Attendence"]] = relationship(back_populates="councilour")

class Attendence(Base):
    __tablename__ = "attendences"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    councilor_id: Mapped[uuid.UUID] = mapped_column(sqlalchemy.ForeignKey("councilours.id"), nullable=False)
    month: Mapped[str] = mapped_column(default=date.today)
    status: Mapped[str] = mapped_column(nullable=False)

    councilour: Mapped["Councilour"] = relationship(back_populates="attendances")

class OfficeSpending(Base):
    __tablename__ = "office_spendings"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    councilor_id: Mapped[uuid.UUID] = mapped_column(sqlalchemy.ForeignKey("councilours.id"), nullable=False)
    month: Mapped[date] = mapped_column(sqlalchemy.Date, nullable=False)
    materials: Mapped[Decimal] = mapped_column(sqlalchemy.Numeric(10, 2), nullable=False, default=Decimal(0))
    mobile_phone: Mapped[Decimal] = mapped_column(sqlalchemy.Numeric(10, 2), nullable=False, default=Decimal(0))
    fixed_phone: Mapped[Decimal] = mapped_column(sqlalchemy.Numeric(10, 2), nullable=False, default=Decimal(0))
    paper: Mapped[Decimal] = mapped_column(sqlalchemy.Numeric(10, 2), nullable=False, default=Decimal(0))
    airline_tickets: Mapped[Decimal] = mapped_column(sqlalchemy.Numeric(10, 2), nullable=False, default=Decimal(0))
    hotel_rate: Mapped[Decimal] = mapped_column(sqlalchemy.Numeric(10, 2), nullable=False, default=Decimal(0))
    gasoline: Mapped[Decimal] = mapped_column(sqlalchemy.Numeric(10, 2), nullable=False, default=Decimal(0))

    councilour: Mapped["Councilour"] = relationship()