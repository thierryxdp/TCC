def total( lista_compras, produtos):
    custo = 0
    for  produtos in lista_compras :
        preco = lista_compras[produtos]
        custo += preco
    return round(custo,2)