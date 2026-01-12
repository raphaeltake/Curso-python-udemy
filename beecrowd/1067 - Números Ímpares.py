x = int(input())
print(*[num for num in range(x+1) if num % 2 != 0], sep='\n')