def total(compras, produtos):
    dinheiro = 0
    for i in range(len(compras)):
        if compras[i] in produtos:
            dinheiro += produtos.get(str(compras[i]))
    return round(dinheiro,2)