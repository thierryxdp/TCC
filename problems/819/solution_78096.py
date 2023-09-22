def filtraMultiplos(lista,n):
    f=[]
    i=0
    while i < len(lista):
        if lista[i]//n==0:
            f.append(lista[i])
            return f