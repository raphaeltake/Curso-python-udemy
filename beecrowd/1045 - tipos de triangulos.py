def verificaTipo(A, B, C):
    if A >= B + C:
        print('NAO FORMA TRIANGULO')
        return

    if A**2 == B**2 + C**2: print("TRIANGULO RETANGULO")
    elif A**2 > B**2 + C**2: print("TRIANGULO OBTUSANGULO")
    elif A**2 < B**2 + C**2: print("TRIANGULO ACUTANGULO")

    if A == B == C: print("TRIANGULO EQUILATERO")
    elif A == B or B == C or C == A: print("TRIANGULO ISOSCELES")
    else: return

A, B, C = map(float, input().split())
dados = [A, B, C]
dados.sort(reverse = True)
A, B, C = dados
verificaTipo(A, B, C)