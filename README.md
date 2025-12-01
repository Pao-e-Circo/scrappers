O `theodoro.py` lê o arquivo .pdf de presença de sessão do último mês especificado em `paoecirco.org_attendences_folder`. O caminho pode ter vários arquivos .pdf, nomeados de `1.pdf` até `12.pdf`, cada um referente à cada mês.

O `ezequiel.py` lê os links do .txt especificados em `paoecirco.org_link.txt_path` e lê, através de scrapping, cada um dos .xlsx dos links.

Ambos salvam os registros na base de dados, vinculado os `concilours` já existentes da base.

Para o ano referência de 2025, a base de `councilours` é:

```
INSERT INTO "councilours" (id,"name",phone,email,photo_url,party) VALUES
	 ('49996a5e-c475-4c10-a06e-3d87682686c1'::uuid,'Ailton De Souza (Ito)','47 3231 1575','ito@camarablu.sc.gov.br','https://camarablu.sc.gov.br/adm/quem_sao/imagens/6255f099705bb/ailton-de-souza-thumb.jpeg','PL'),
	 ('fd21f3bf-018a-41f0-b7ff-324a353a58f6'::uuid,'Diego Nasato','47 992805451','diego.nasato@camarablu.sc.gov.br','https://camarablu.sc.gov.br/adm/quem_sao/imagens/6399e22eae26f/diego-nasato-thumb.jpg','NOVO'),
	 ('368d5547-239e-4be6-99be-f2aa15393ad8'::uuid,'Cristiane Loureiro','47 991199010','cristianeloureiro@camarablu.sc.gov.br','https://camarablu.sc.gov.br/adm/quem_sao/imagens/6255f48dab317/cristiane-loureiro-thumb.jpg','PODEMOS'),
	 ('9d117cd7-2f84-4595-9d2e-cccaef96f329'::uuid,'Egídio Da Rosa Beckhauser',NULL,'egidiobeckhauser@camarablu.sc.gov.br','https://camarablu.sc.gov.br/adm/quem_sao/imagens/6255d8b410a08/egidio-da-rosa-beckhauser-thumb.jpg','REPUBLICANOS'),
	 ('bc93c075-55f0-4eb5-a574-a5d5dc3c380e'::uuid,'Mário Kato',NULL,NULL,'https://camarablu.sc.gov.br/adm/quem_sao/imagens/691d9e8c24954/mrio-kato-thumb.png','PT'),
	 ('6cfdb342-e0d3-41fe-b425-44c2ceb38a34'::uuid,'Alexandre Matias','47 99915 4545','gabinete@alexandrematias.com','https://camarablu.sc.gov.br/adm/quem_sao/imagens/6255f209111fb/alexandre-matias-thumb.jpeg','PSDB'),
	 ('b8d198ee-ea54-45b8-82e5-28034c7bc341'::uuid,'Almir Vieira','47 988210619','almirvieira@camarablu.sc.gov.br','https://camarablu.sc.gov.br/adm/quem_sao/imagens/6255e4e68e51d/almir-vieira-thumb.jpg','PP'),
	 ('a146e11c-7f88-4d41-ad3b-a0528b164399'::uuid,'Bruno Cunha','47 997353432','brunocunha@camarablu.sc.gov.br','https://camarablu.sc.gov.br/adm/quem_sao/imagens/6255f2c89232f/bruno-cunha-thumb.jpg','CIDADANIA'),
	 ('625b408e-3ef7-4660-acab-1b9b2078280a'::uuid,'Bruno Win','47 99239 7878','brunowin@camarablu.sc.gov.br','https://camarablu.sc.gov.br/adm/quem_sao/imagens/67f6d86271916/bruno-ricardo-winzewski-thumb.png','NOVO'),
	 ('89cea5b7-dedf-4d8b-a151-3342f12579d3'::uuid,'Flávio José Linhares (Flavinho)','47 3231 1520','flavinho@camarablu.sc.gov.br','https://camarablu.sc.gov.br/adm/quem_sao/imagens/6784f459e2f07/flvio-jos-linharesflavinho-thumb.jpg','PL');
INSERT INTO "councilours" (id,"name",phone,email,photo_url,party) VALUES
	 ('5bdc8b14-67c9-4223-9bfa-fc95fea0bb70'::uuid,'Gilson De Souza','47 999230218','professorgilson@camarablu.sc.gov.br','https://camarablu.sc.gov.br/adm/quem_sao/imagens/6255f62c1c14f/gilson-de-souza-thumb.jpg','União Brasil'),
	 ('bf3ad12a-0695-402c-917b-a7b32c1a26ee'::uuid,'Jean Volpato',NULL,'jeanvolpato@camarablu.sc.gov.br','https://camarablu.sc.gov.br/adm/quem_sao/imagens/6784f84c2cf2e/jean-volpato--thumb.jpeg','PT'),
	 ('b7d38f7d-6f4a-401a-a586-f4a4a1ad43ee'::uuid,'Jovino Cardoso Neto','47 996359820','jovinocardoso@camarablu.sc.gov.br','https://camarablu.sc.gov.br/adm/quem_sao/imagens/6255f7415ecb8/jovino-cardoso-neto-thumb.jpg','PL'),
	 ('8479bdf6-b2a6-428b-8f1c-61c98be04b07'::uuid,'Marcelo Lanzarin','47 3231 1506/1605','drmarcelolanzarin@camarablu.sc.gov.br','https://camarablu.sc.gov.br/adm/quem_sao/imagens/66155cbbb886e/marcelo-lanzarin-thumb.jpg','PP'),
	 ('5410d894-a51f-47cb-9225-e68bdacdfced'::uuid,'Silmara Miguel','47 996141155','vereadorasilmaramiguel@camarablu.sc.gov.br','https://camarablu.sc.gov.br/adm/quem_sao/imagens/6255dd556a6c4/silmara-miguel-thumb.jpg','PSD');

```
