import os
import requests
import json
from pymongo import MongoClient
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# para acessar as variáveis
url_database = os.getenv("URL_MONGO_DB")
json_file = os.getenv("URL_JSON")

# Pasta onde o arquivo será salvo localmente
pasta_destino = "./json_files"

# Nome do arquivo para verificar
nome_arquivo = "dados_de_municipios.json"

# Caminho para o arquivo
caminho_arquivo = os.path.join(pasta_destino, nome_arquivo)

# Verifica se o arquivo existe
if os.path.exists(caminho_arquivo):
    print(f"O arquivo {nome_arquivo} já existe em {pasta_destino}.")
else:
    # Baixa o arquivo JSON da URL
    response = requests.get(json_file)

    # Especifica manualmente a codificação ao carregar o JSON
    dados_json = json.loads(response.content.decode('utf-8-sig'))

    # Salva o arquivo na pasta local
    nome_arquivo = os.path.join(pasta_destino, "dados_municipio.json")
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo_local:
        json.dump(dados_json, arquivo_local, ensure_ascii=False)

        # Conecta-se ao MongoDB e cria um banco de dados e uma coleção
        cliente = MongoClient(url_database)
        banco_dados = cliente["municipios_do_brasil"]
        colecao = banco_dados["municipios"]

    # Verifica se o banco de dados já existe
    lista_bancos = cliente.list_database_names()
    if "municipios_do_brasil" in lista_bancos:
        print("O banco de dados 'municipios_do_brasil' já existe.")
    else:
        # Insere os dados do arquivo JSON no MongoDB
        colecao.insert_many(dados_json)
        print("Dados inseridos no MongoDB com sucesso!")


municipios_de_rondonia = colecao.find({"Uf": "RO"})

try:
    print("Municipios de Rondonia:")
    for municipio in municipios_de_rondonia:
        print(municipio)

except Exception as error:
    print("Erro ao consultar Municipios:", error)
