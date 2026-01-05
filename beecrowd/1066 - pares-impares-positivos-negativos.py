pares, impares, positivos, negativos = 0, 0, 0, 0
for i in range(5):
    valor = float(input())
    if valor % 2 == 0: pares += 1
    else: impares += 1
    if valor > 0: positivos += 1
    elif valor < 0: negativos += 1
print(f'{pares} valor(es) par(es)')
print(f'{impares} valor(es) impar(es)')
print(f'{positivos} valor(es) positivos(s)')
print(f'{negativos} valor(es) negativos(s)')
