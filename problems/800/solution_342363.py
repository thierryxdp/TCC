def total(compras, precos):
    custo_final = 0
    for item in compras:
        if item in precos:
            custo_final += precos[item]
    return round(custo_final, 2)