def total(lista, produtos):
    fiscal = 0
    for l in lista:
        for p in produtos:
            if l == p:
                fiscal += produtos.get(p)
    return(fiscal)