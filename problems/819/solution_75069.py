def filtraMultiplos(lista,n):
    cont=0
    div=[]
    while cont<len(lista):
        if lista[cont]%n==0:
            list.append(lista[cont])
        cont+=1
    return div