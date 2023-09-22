def filtraMultiplos(lista,n):
    f=[]
    i=0
    while i < len(lista):
        if lista[i]%n==0:
            f.append(lista[i])
            i=i+1
        else:
            i=i+1
            return f