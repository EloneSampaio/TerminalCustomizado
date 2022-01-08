from model import Pet


def create_pet(pets):
    pet = Pet.insert_many(pets).execute()
    return pet

def search_pet(nome):
    pet = Pet.get(Pet.nome == nome)
    return pet
def search_pet_by_categoria(categoria):
    pets = Pet.select().where(Pet.categoria == categoria)
    return pets
def update_pet_nome(nome, novo_nome):
    try:
        pet = Pet.get(Pet.nome == nome)
        if pet is not None:
            pet.nome = novo_nome
            pet.save()
            return pet
        else:
            print('Pet não encontrado!')
    except Exception as e:
        print(e)
def delete_pet(nome):
    pet = Pet.get(Pet.nome == nome)
    return pet.delete_instance()
def getAll():
    pets = Pet.select()
    return pets


if __name__ == '__main__':
    
    pet=delete_pet('Sabrina')
    if pet:
        print('Deletado com sucesso!')
    else:
        print('Pet não encontrado!')
    