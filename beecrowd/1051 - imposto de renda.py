def calculaImposto(renda):
    valor_imposto = 0.0
    if renda > 4500.00:
        valor_imposto = (renda - 4500) * 0.28
        renda = 4500.00
    if renda > 3000.00:
        valor_imposto += (renda - 3000) * 0.18
        renda = 3000.00
    if renda > 2000.00:
        valor_imposto += (renda - 2000) * 0.08
    else:
        return
    return valor_imposto

renda_declarada = float(input())
valor_imposto = calculaImposto(renda_declarada)
print(f"R$ {valor_imposto:.2f}" if isinstance(valor_imposto, float) else "Isento")