def filtraMultiplos(lista, n):
    i=0
    lista2=()

    while i<len(lista):
        if lista[i]%n==0:
            x=int(lista[i])
            lista2[i]=x
        i=i+1

    return lista2