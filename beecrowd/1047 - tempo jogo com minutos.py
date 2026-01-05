# def calcula_hora(hora_inicial, minuto_inicial, hora_final, minuto_final):
#     if hora_inicial == hora_final and minuto_inicial == minuto_final: return 24
#     if hora_inicial > hora_final: return (24 - hora_inicial) + hora_final
#     return hora_final - hora_inicial
#
# def calcula_minutos(minuto_inicial, minuto_final):
#     return minuto_final - minuto_inicial
#
# hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split(" "))
# horas_totais = calcula_hora(hora_inicial, minuto_inicial, hora_final, minuto_final)
# minutos_totais = calcula_minutos(minuto_inicial, minuto_final)
#
# if minutos_totais < 0:
#     if horas_totais > 0:
#         horas_totais -= 1
#     minutos_totais += 60
#
#
# print(f"O JOGO DUROU {horas_totais} HORA(S) E {minutos_totais} MINUTO(S)")


hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split(" "))

inicio_jogo = hora_inicial * 60 + minuto_inicial
fim_jogo = hora_final * 60 + minuto_final

if fim_jogo <= inicio_jogo:
    fim_jogo += 24 * 60

duracao = fim_jogo - inicio_jogo
horas = duracao // 60
minutos = duracao % 60

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
