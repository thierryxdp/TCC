def total(lista, produtos):
    fical = 0
    for l in lista:
        for p in produtos:
            if l == p:
                fical += produtos.get(p)
    return(fiscal)