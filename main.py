from unicodedata import name
from db.database import Database
from helper.WriteAJson import writeAJson

db = Database("db", "livros")

db.create("1", "Clean Code", "Robert C. Martin", 2008, 31.0)
db.create("2", "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997, 31.0)
db.create("3", "As cidades invisíveis", "Italo Calvino", 1972, 67.83)

db.read()

db.update("Harry Potter and the Philosopher's Stone", 45.5)

db.delete("Clean Code")

db.read()
