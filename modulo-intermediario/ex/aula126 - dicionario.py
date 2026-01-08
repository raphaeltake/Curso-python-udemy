# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

pontos = 0

for i in perguntas:
  print(f"\nPergunta: {i["Pergunta"]}")
  print("Opções: ")
  for j in range(len(i["Opções"])):
    print(f"{j}) {i["Opções"][j]}")
  resposta = input("Escolha uma opção: ")
  if resposta.isdigit() and i["Opções"][int(resposta)] == i["Resposta"]:
    pontos += 1
    print("Certo 👍")
    continue
  print("Errado ❌")

print(f"Você acertou {pontos} de 3 questões")

