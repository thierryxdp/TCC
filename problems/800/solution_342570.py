def total(ls_compras, produtos = {}):
    novalista = []
    for e in ls_compras:
        if e in produtos.keys():
            novalista = produtos[e]
            soma = sum(novalista)
            
            return soma