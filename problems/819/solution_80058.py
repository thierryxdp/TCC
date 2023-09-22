def filtraMultiplos(lista,n):
    f=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            f=list.insert(f,i,lista[i])
            i=i+1
    return f