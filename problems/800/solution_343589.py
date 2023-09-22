def total( lista_compras, produtos):
    custo = 0
    for   lista_compras in produtos :
        preco = lista_compras[produtos]
        custo += preco
    return round(custo,2)