def total( lista_compras, produtos):
    custo = 0
    for produto in produtos:
        preco = lista_compra[produto]
        custo += preco
    return round(custo,2)