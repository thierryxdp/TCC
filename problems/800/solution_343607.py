def total( lista_compras, produtos):
    
    custo = 0
    for compra in lista_compras:
        preco = produtos[compra]
        custo += preco
    return round(custo,2)