def total(ls_compras, produtos = {}):
    novalista = []
    for e in ls_compras:
        if e in produtos.keys():
            novalista += [produtos[e]]
    return sum(novalista)
    return novalista