def repetidos (lista):
    i=1
    lista1 = []
    while i<len(lista):
        if lista[i] == lista [i+1]:
            lista1 = lista1 + [1]
            return 
        i = i+1 
    return sum(lista1)