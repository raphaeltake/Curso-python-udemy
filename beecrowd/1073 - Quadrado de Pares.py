n = int(input())
print(*[f"{num}^2 = {num**2}" for num in range(2,n+1) if num % 2 == 0], sep="\n")