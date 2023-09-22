def filtraMultiplos(lista,n):
    multiplos=[]
    i=0
    while i<=len(lista)-1:
        if lista[i]%n==0:
            list.append(multiplos,lista[i])
            i=i+1
        elif i<=len(lista):
            lista[i]%n!=0
            i=i+1
    return multiplos