import typer
from rich.console import Console
from rich.table import Table
from rich import print

from crud import *
from helpers import read_json_file
from database import create_database

console = Console()
app = typer.Typer()

@app.command()
def show(pets):
    tabela = Table(show_header=True, header_style="bold red")
    tabela.add_column("Nome", justify="left", style="bold green")
    tabela.add_column("Categoria", justify="left", style="bold green")
    tabela.add_column("Idade", justify="left", style="bold green")
    tabela.add_column("Raça", justify="left", style="bold green")
    tabela.add_column("Responsavel", justify="left", style="bold green")
        
    if pets is None:
        tabela.add_row("Nenhum pet cadastrado")
        print(tabela)
    else:
        for p in pets:
            tabela.add_row(p.nome, p.categoria, str(p.idade), p.raca, p.responsavel)
        print(tabela)


@app.command()
def tabelas():
    typer.echo(f'\nTabelas:')
    create_database()

@app.command()
def listartodos():
    typer.echo(f'\nListar todos os pets:')
    pets = getAll()
    show(pets)
@app.command()
def add(file:str=typer.Argument(..., help='Dados do Pet a ser criado')):
    typer.echo (f'\nCriando pet...')
    pets = read_json_file(file)
    create_pet(pets)
    
@app.command()
def pesquisarpet(nome:str=typer.Argument(..., help='Nome do Pet a ser pesquisado')):
    typer.echo (f'\nProcurando pet...')
    p=search_pet(nome)
    show([p])
    
@app.command()
def pesquisarpetbycategoria(categoria:str=typer.Argument(..., help='Categoria do Pet a ser pesquisado')):
    typer.echo (f'\nProcurando pet por categoria...')
    p=search_pet_by_categoria(categoria)
    show(p)
        
@app.command()
@app.command()  
def atualizarpetbynome(nome:str=typer.Argument(..., help='Nome do Pet a ser atualizado'), novonome:str=typer.Argument(..., help='Novo nome do Pet')):
    typer.echo (f'\nAtualizando nome...')
    p = update_pet_nome(nome, novonome)
    show([p])
    
@app.command()
def removerpet(nome:str=typer.Argument(..., help='Nome do Pet a ser removido')):
    typer.echo (f'\nDeletando pet...')
    delete_pet(nome)
    p = getAll()
    show(p)
    
if __name__ == '__main__':
    app()