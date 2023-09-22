def total (compras,precos):
    ''''''
    valores = []
    for item in compras:
        valores += precos[item]
    return list.sum(valores)