def repetidos(l):
    lista = 0
    proximo = 0 
    while proximo <len(l):
        if l[proximo] == l[proximo -1] :
            lista = lista + 1
    return lista