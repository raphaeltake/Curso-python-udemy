x = int(input())
impares = []
while len(impares) != 6:
  if x % 2 != 0: impares.append(x)
  x+= 1

print(*impares, sep="\n")