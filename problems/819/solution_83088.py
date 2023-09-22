def filtraMultiplos(lista,n):
    nova=[]
    i=0
    while lista[i]<len(lista):
        if lista[i]%n==0:
            list.append(nova,lista[i])
        i=i+1
    return nova