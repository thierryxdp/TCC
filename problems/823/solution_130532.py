def faltante(lista):
    lista1=[]
    i=0
    lista.sort()
    while i < (len(lista)-1):
        if lista[i+1] - lista[i] >1:
            return i+2
        i+=1
    if lista[0] == 1:
        return lista[-1] + 1
    else:
        return lista[0] -1