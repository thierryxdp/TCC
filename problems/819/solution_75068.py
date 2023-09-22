def filtraMultiplos(lista,n):
    cont=0
    div=0
    while cont<len(lista):
        if lista[cont]%n==0:
            div+=1
        cont+=1
    return div