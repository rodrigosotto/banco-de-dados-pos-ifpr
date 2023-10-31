# libs
import firebase_admin
from firebase_admin import credentials, db

# Aqui eu Inicializo o SDK do Firebase com as minhas credenciais.
cred = credentials.Certificate(
    "./banco-de-dados-das-coisas-firebase-adminsdk-gmhfb-6d4431584b.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://banco-de-dados-das-coisas-default-rtdb.firebaseio.com/'
})

# referenciando o meu banco de dados.
ref = db.reference('/aula1')

# Aqui Adiciono uma chave e valor ao banco de dados para ser mostrado la no banco de dados.
chave = 'Sobrenome'
valor = 'Sotto'

ref.update({chave: valor})

print(f'Chave {chave} adicionada com o valor {valor}, obrigado!')
