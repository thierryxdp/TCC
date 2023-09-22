def total(compras,precos):
    """Retorna o valor total a pagar em uma compra a partir da lista
    de produtos e da lista de preços. (list,dict->float)"""
    pagar=0
    for i in compras:
        if i in precos:
            pagar=pagar+precos[i]
    return round(pagar,2)