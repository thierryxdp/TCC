def total(lista, produtos):
    c = 0
    l = []
    for x in produtos:
        if lista in produtos[x]:
             l = l + [produtos[x]]
        c = c + 1
        
        return sum(l)