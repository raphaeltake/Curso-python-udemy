"""
Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro
"""

def cria_multiplicador(multiplicador):
  def calcular(numero):
    return numero * multiplicador
  return calcular

duplicar = cria_multiplicador(2)
triplicar = cria_multiplicador(3)
quadruplicar = cria_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))