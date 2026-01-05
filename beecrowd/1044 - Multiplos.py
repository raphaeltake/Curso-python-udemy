def verifica(x, y):
    print('Sao Multiplos' if x % y == 0 or y % x == 0 else 'Nao sao Multiplos')

x, y = map(int, input().split())
verifica(x, y)
