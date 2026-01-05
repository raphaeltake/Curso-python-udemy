n = int(input())
In = 0
Out = 0
for i in range(n):
  valor = int(input())
  if 10 <= valor <= 20:
    In += 1
  else:
    Out += 1

print(f'{In} in')
print(f'{Out} out')