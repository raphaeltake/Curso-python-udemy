valor = int(input())

ano = 0
mes = 0
dia = 0

while valor >= 365:
    ano +=1
    valor -= 365

while valor >= 30:
    mes += 1
    valor -= 30

dia = valor

print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{dia} dia(s)')
