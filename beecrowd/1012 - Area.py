valores = input()

A, B, C = valores.split()

A = float(A)
B = float(B)
C = float(C)

pi = 3.14159

triRetangulo =(A * C) / 2

areaCirculo = pi * C**2

areaTrapezio = ((A+B) * C)/ 2

ladoQuadrado = B**2

areaRetangulo = A * B

print(f'TRIANGULO: {triRetangulo:.3f}')
print(f'CIRCULO: {areaCirculo:.3f}')
print(f'TRAPEZIO: {areaTrapezio:.3f}')
print(f'QUADRADO: {ladoQuadrado:.3f}')
print(f'RETANGULO: {areaRetangulo:.3f}')

