def filtraMultiplos(lista, numero):
    numeros=[]
    a= 0
    while a <len(lista):
        if lista [a]%numero == 0:
            numeros= numeros + [lista[a],]
        a= a+1
    return numeros