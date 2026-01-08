"""
Pedrinho está organizando um evento em sua Universidade. O evento deverá ser no mês de Abril, iniciando e terminando dentro do mês. O problema é que Pedrinho quer calcular o tempo que o evento vai durar, uma vez que ele sabe quando inicia e quando termina o evento.

Sabendo que o evento pode durar de poucos segundos a vários dias, você deverá ajudar Pedrinho a calcular a duração deste evento.

Entrada
Como entrada, na primeira linha vai haver a descrição “Dia”, seguido de um espaço e o dia do mês no qual o evento vai começar. Na linha seguinte, será informado o momento no qual o evento vai iniciar, no formato hh : mm : ss. Na terceira e quarta linha de entrada haverá outra informação no mesmo formato das duas primeiras linhas, indicando o término do evento.

Saída
Na saída, deve ser apresentada a duração do evento, no seguinte formato:

W dia(s)
X hora(s)
Y minuto(s)
Z segundo(s)

Obs: Considere que o evento do caso de teste para o problema tem duração mínima de 1 minuto.

Exemplo de Entrada
Dia 5
08 : 12 : 23
Dia 9
06 : 13 : 23

Exemplo de Saída
3 dia(s)
22 hora(s)
1 minuto(s)
0 segundo(s)
"""

def calcular_tempo_total():
  def calcular_tempo():
    inicio_em_segundos = (dia_inicio * 24 * 3600) + (horario_inicio[0] * 3600) + (horario_inicio[1] * 60) + horario_inicio[2]
    fim_em_segundos = (dia_fim * 24 * 3600) + (horario_fim[0] * 3600) + (horario_fim[1] * 60) + horario_fim[2]
    
    duracao = fim_em_segundos - inicio_em_segundos

    dias = duracao // (24 * 3600)
    duracao %= 24 * 3600

    horas = duracao // 3600
    duracao %= 3600

    minutos = duracao // 60
    segundos = duracao % 60

    return dias, horas, minutos, segundos
  
  def exibir_tempo():
    print(f"{dias} dia(s)")
    print(f"{horas} hora(s)")
    print(f"{minutos} minuto(s)")
    print(f"{segundos} segundo(s)")

  dias, horas, minutos, segundos = calcular_tempo()

  exibir_tempo()

dia_inicio = int(input().split(" ")[1])
horario_inicio = list(map(int, input().split(" : ")))
dia_fim = int(input().split(" ")[1])
horario_fim = list(map(int, input().split(" : ")))
calcular_tempo_total()