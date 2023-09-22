def mariores(lista,n):
    y = lista
    for i in range(len(lista)):
        if lista[i]<n:
            del y[i]             
            return [y]