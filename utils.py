from models import Pessoas, Tarefas

# função para inserir uma pessoa
def insere_pessoa():
    pessoa = Pessoas(nome='Beltrano', idade=30)
    pessoa.save()

def lista_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)

def consulta_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Fulano').first()
    print(pessoa.id)

def atualiza_pessoa():
    pessoa = Pessoas.query.filter_by(id=2).first()
    pessoa.nome = "Cicrano"
    pessoa.save()

def remove_pessoa():
    pessoa = Pessoas.query.filter_by(id=2).first()
    pessoa.delete()

# função para inserir uma pessoa
def insere_tarefa():
    tarefa = Tarefas(titulo='Comprar fraldas', fk_pessoa_id=1)
    tarefa.save()

def lista_tarefas():
    tarefas = Tarefas.query.all()
    print(tarefas)

def consulta_tarefa():
    tarefa = Tarefas.query.filter_by(titulo='Comprar fralda').first()
    print(tarefa.titulo)

def atualiza_tarefa():
    tarefa = Tarefas.query.filter_by(id=1).first()
    tarefa.titulo = "Comprar fralda"
    tarefa.save()

def remove_tarefa():
    tarefa = Tarefas.query.filter_by(id=1).first()
    tarefa.delete()

if __name__ == '__main__':
    # insere_pessoa()
    # consulta_pessoa()
    # atualiza_pessoa()
    # remove_pessoa()
    # lista_pessoas()
    # insere_tarefa()
    # atualiza_tarefa()
    # consulta_tarefa()
    remove_tarefa()
    lista_tarefas()
