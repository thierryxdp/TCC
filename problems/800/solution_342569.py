def total(ls_compras, produtos = {}):
   
    for e in ls_compras:
        if e in produtos.keys():
            soma = sum(produtos.values())
            
            return soma