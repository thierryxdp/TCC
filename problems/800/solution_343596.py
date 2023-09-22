def total( lista_compras, produtos):
    custo = 0
    for produto in produtos:
        preco = produtos[produto]
        custo += preco
        return round(custo,2)