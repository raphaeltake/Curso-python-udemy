qtde = 0
media = 0

for i in range(6):
    valor = float(input())
    if valor > 0:
        qtde += 1
        media += valor

media = media / qtde
print(f'{qtde} valores positivos')
print(f'{media:.1f}')