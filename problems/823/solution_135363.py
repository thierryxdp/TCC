def faltante(lista):
    i=0
    a=0
    if lista[0]==1:
        return lista[0]+1
    while i<len(lista)-1:
        if lista[i+1] != lista[i] +1:
            return lista[i+1]
        i+=1