def total(ls_compras, produtos = {}):
    novalista = []
    for e in ls_compras:
        if e in produtos.keys():
            novalista += [produtos[e]]
    return round(sum(novalista),2)
    return novalista