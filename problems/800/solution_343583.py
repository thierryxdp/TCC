def total( lista_compras, produtos):
    custo = 0
    for lista_compras in produtos:
        preco = produtos[lista_compras]
        custo += preco
        return round(custo,2)