def  total(l,d):
    """Pegamos cada elemento da lista de compra, comparamos seu preço e somamos.
    str,dicionario-->int
    """
    t=0
    for compras in l:
        t+=d[compras]
    return round(t,2)