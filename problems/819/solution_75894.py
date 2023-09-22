def filtraMultiplos(lista,n):
    i=0
    multiplo=[]
    while i<len(lista):
        if lista[i]%n==0:
            list.append(multiplo,lista[i])
        i=i+1
    return multiplo