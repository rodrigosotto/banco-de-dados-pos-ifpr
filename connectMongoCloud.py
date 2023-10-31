from pymongo import MongoClient

uri = "mongodb+srv://jrsottodev:30302220@cluster0.jowzjzk.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")

    # Salva em uma variável o nosso banco de dados
    db = client.get_database('sample_mflix')
    
    # Lista as "tabelas" do banco
    collections = db.list_collection_names()

    # Imprime o nome das coleções
    print("Coleções no banco de dados:")
    for collection in collections:
        print(collection)

except Exception as e:
    print("Erro ao conectar ao MongoDB:", e)
