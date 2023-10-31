import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# para acessar as variáveis
url_database = os.getenv("URL_MONGO_DB")
json_file = os.getenv("URL_JSON")

# Conecta-se ao MongoDB e cria um banco de dados e uma coleção
cliente = MongoClient(url_database)
banco_dados = cliente["municipios_do_brasil"]
colecao = banco_dados["municipios"]

municipios_de_rondonia = colecao.find({"Uf": "RO"})

try:
    print("Municipios de Rondonia:")
    for municipio in municipios_de_rondonia:
        print(municipio)

except Exception as error:
    print("Erro ao consultar Municipios:", error)