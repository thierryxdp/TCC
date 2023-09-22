filtraMultiplos(lista, n):
    i=0
    lista_mult=[]
    while i<len(lista):
        if lista[i]%n==0:
            lista_mult=lista_mult+[n]
        i+=1
    return lista_mult