def total(compras,estoque):
    """ cospe o preço total do que vc tem na sua lista
    de compras e oq tem no estoque list, dict -> int """
    vt = 0
    for compra in compras :
        if compra in estoque :
            vt = vt + estoque[compra]
        else:
            vt = vt
    return round(vt,2)