import peewee

def create_database():
    db = peewee.SqliteDatabase('pets.db')
    return db