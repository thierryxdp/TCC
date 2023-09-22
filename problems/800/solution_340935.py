def total(lista, produtos):
    c = 0
    l = []
    for x in produtos:
        if lista[c] in produtos:
             l = l + x
        c = c + 1
        
        return sum(l)