def total(ls_compras, produtos = {}):
   
    for e in ls_compras:
        if e in produtos:
            soma = sum(produtos.values())
            return soma