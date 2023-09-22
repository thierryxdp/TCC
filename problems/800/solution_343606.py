def total( lista_compras, produtos):
    custo = 0
    for alimento in lista_compras:
        preco = produtos[alimento]
        custo += preco
    return round(custo,2)