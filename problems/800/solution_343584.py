def total( lista_compras, produtos):
    custo = 0
    for produtos in lista_compras:
        preco = produtos[lista_compras]
        custo += preco
    return round(custo,2)