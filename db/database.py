import pymongo

from helper.WriteAJson import writeAJson


class Database:
    def __init__(self, database, collection, dataset=None):
        connectionString = "mongodb+srv://adm:adm@cluster0.7vj9c.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        self.clusterConnection = pymongo.MongoClient(
            connectionString,
            # CASO OCORRA O ERRO [SSL_INVALID_CERTIFICATE]
            tlsAllowInvalidCertificates=True
        )
        self.db = self.clusterConnection[database]
        self.collection = self.db[collection]
        if dataset:
            self.dataset = dataset

    def resetDatabase(self):
        self.db.drop_collection(self.collection)
        self.collection.insert_many(self.dataset)

    def read(self):
        livros = self.collection.find({})
        writeAJson(livros, "Livros")

    def update(self, nome, preco):
        return self.collection.update_one(
            {"nome": nome},
            {
                "$set": {"preco": preco},
                "$currentDate": {"lastModified": True}
            }
        )

    def delete(self, nome):
        return self.collection.delete_one({"nome": nome})

    def create(self, id, nome, autor, ano, preco):
        return self.collection.insert_one({"_id": id, "nome": nome, "autor": autor, "ano": ano, "preco": preco})

