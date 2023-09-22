def total(lis_compra,preco_produto):
    preco_total=0
    for i in lis_compra:
        if i in preco_produto:
            preco_total=preco_total+preco_produto[i]
    return preco_total