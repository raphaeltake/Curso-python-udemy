def calcularNotas(dinheiros):
    notas = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0}

    for valores in notas.keys():
        qtde = dinheiros // valores
        dinheiros = dinheiros - qtde * valores
        notas[valores] = qtde

    calcularMoedas(int(dinheiros * 100), notas)

def calcularMoedas(dinheiros, notas):
    moedas = {100: 0, 50: 0, 25: 0, 10: 0, 5: 0, 1: 0}

    for valores in moedas.keys():
        qtde = dinheiros // valores
        dinheiros = dinheiros - qtde * valores
        moedas[valores] = qtde

    exibirNotas(moedas, notas)

def exibirNotas(moedas, notas):
    print('NOTAS:')
    for notas, qtde in notas.items():
        print(f'{int(qtde)} nota(s) de R$ {notas:.2f}')

    print('MOEDAS:')
    for moedas, qtde in moedas.items():
        print(f'{qtde} moeda(s) de R$ {(moedas / 100):.2f}')

calcularNotas(float(input()))



















# valor = float(input())
#
# nota100 = 0
# nota50 = 0
# nota20 = 0
# nota10 = 0
# nota5 = 0
# nota2 = 0
#
# moeda1 = 0
# moeda05 = 0
# moeda025 = 0
# moeda010 = 0
# moeda005 = 0
# moeda001 = 0
#
# while valor >= 100:
#     nota100 += 1
#     valor -= 100
#
# while valor >= 50:
#     nota50 += 1
#     valor -= 50
#
# while valor >= 20:
#     nota20 += 1
#     valor -= 20
#
# while valor >=10:
#     nota10 += 1
#     valor -= 10
#
# while valor >= 5:
#     nota5 += 1
#     valor -= 5
#
# while valor >= 2:
#     nota2 += 1
#     valor -= 2
#
# while valor >= 1:
#     moeda1 += 1
#     valor -= 1
#
# while valor >= 0.5:
#     moeda05 += 1
#     valor -= 0.5
#
# while valor >= 0.25:
#     moeda025 += 1
#     valor -= 0.25
#
# while valor >= 0.1:
#     moeda010 += 1
#     valor -= 0.1
#
# while valor >= 0.05:
#     moeda005 += 1
#     valor -= 0.05
#
#
# while valor >= 0:
#     moeda001 += 1
#     valor -= 0.01
#
# print('NOTAS:')
# print(f'{nota100} nota(s) de R$ 100.00')
# print(f'{nota50} nota(s) de R$ 50.00')
# print(f'{nota20} nota(s) de R$ 20.00')
# print(f'{nota10} nota(s) de R$ 10.00')
# print(f'{nota5} nota(s) de R$ 5.00')
# print(f'{nota2} nota(s) de R$ 2.00')
# print('MOEDAS:')
# print(f'{moeda1} moeda(s) de R$ 1.00')
# print(f'{moeda05} moeda(s) de R$ 0.50')
# print(f'{moeda025} moeda(s) de R$ 0.25')
# print(f'{moeda010} moeda(s) de R$ 0.10')
# print(f'{moeda005} moeda(s) de R$ 0.05')
# print(f'{moeda001} moeda(s) de R$ 0.01')

