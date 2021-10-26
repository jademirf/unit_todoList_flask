from models import Pessoas

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

if __name__ == '__main__':
    # insere_pessoa()
    # consulta_pessoa()
    # atualiza_pessoa()
    remove_pessoa()
    lista_pessoas()
