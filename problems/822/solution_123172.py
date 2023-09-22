def repetidos(l):
    lista = 0
    i = 1 
    while i <len(l):
        if l[i] == l[i-1] :
            lista = lista + 1
    return lista