from enum import unique
import peewee
from database import create_database

class BaseModel(peewee.Model):
    class Meta:
        database = create_database()

class Pet(BaseModel):
    nome = peewee.CharField(unique=True)
    categoria = peewee.CharField()
    peso = peewee.FloatField()
    idade = peewee.IntegerField()
    responsavel = peewee.CharField()
    raca = peewee.CharField()
    
if __name__ == '__main__':
    try:
        Pet.create_table()
        print('Tabela criada com sucesso!')
    except peewee.OperationalError:
        print('Tabela já existe!')