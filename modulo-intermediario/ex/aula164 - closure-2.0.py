"""
# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, *args):
    return funcao(*args)


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)
"""
def cria_soma(x):
  def soma(y):
    return x + y
  return soma

def cria_multiplicador(x):
  def multiplica(y):
    return x * y
  return multiplica

def criar_funcao(funcao, *args):
    return funcao(*args)

soma = cria_soma(5)
multiplica = cria_multiplicador(10)
soma_com_cinco = criar_funcao(soma, 10)
multiplica_por_dez = criar_funcao(multiplica, 20)
print(soma_com_cinco)
print(multiplica_por_dez)