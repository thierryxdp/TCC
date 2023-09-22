def faltante(lista):
    i=0
    if lista[0]!=1:
        return 1
    while i<len(lista)-1:
        if abs((lista[i])-(lista[i+1]))!=1:
            return lista[i+1]-1
        i=i+1
    else:
        return lista + list(lista[-1]+1)