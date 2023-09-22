def mariores(lista,n):
    y = lista
    for i in range(len(lista)):
        if lista[i]<n:
            y = del y[i]             
            return [y]