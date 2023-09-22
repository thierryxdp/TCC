def filtraMultiplos(lista,n):
    i=0
    lista2=[]
    while i<len(lista):
        if lista[i]%n==0:
            lista2.append(lista[i])
            i+=1
        else:
            i+=1
    return lista2