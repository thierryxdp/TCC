def total(ls_compras, produtos = {}):
    novalista = []
    for e in ls_compras:
        if e in produtos.keys():
            novalista = sum(produtos[e])            
            return novalista