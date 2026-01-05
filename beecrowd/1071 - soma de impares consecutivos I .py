x = int(input())
y = int(input())
if y > x: 
  x, y = y, x
soma = 0
for i in range(y + 1, x):
  if i % 2 == 1:
    soma += i
print(soma)