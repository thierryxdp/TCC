def filtraMultiplos(lista,n):
    lista2=[]
    for i in lista:
        if i%n==0:
            lista2.append(i)
    return(lista2)