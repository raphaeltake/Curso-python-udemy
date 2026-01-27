"""
copy, sorted, produtos.sort
Exercícios
Aumente os preços dos produtos a seguir em 10%
Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

Ordene os produtos por nome decrescente (do maior para menor)
Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

Ordene os produtos por preco crescente (do menor para maior)
Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
"""

import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = [
  {"nome": produto["nome"], "preco": produto["preco"] * 1.10}
  for produto in copy.deepcopy(produtos)
]
print(novos_produtos)


# 2 ---------------------------------------------------
novos_produtos_decrescente = sorted(novos_produtos, key=lambda produto: produto["nome"], reverse=True)

print()
print(novos_produtos_decrescente)

# 3 ---------------------------------------------------
novos_produtos_cescente = sorted(novos_produtos, key=lambda produto: produto["nome"], reverse=False)

print()
print(novos_produtos_cescente)