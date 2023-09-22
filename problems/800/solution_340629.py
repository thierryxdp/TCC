def total (compras,preços):
    ''''''
    valores = []
    for item in compras:
        valores += preços[item]
    return list.sum(valores)