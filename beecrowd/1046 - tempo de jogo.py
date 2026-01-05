def calculaHora(inicio, fim):
    if fim > inicio: return  fim - inicio

    ate24horas = 24 - inicio
    return ate24horas + fim

inicio, fim = map(int, input().split())
print(f'O JOGO DUROU {calculaHora(inicio, fim)} HORA(S)')