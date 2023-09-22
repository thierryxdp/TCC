def filtraMultiplos(lista,n):
    f=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            f= f+(f[i],)
            else:
                i=i+1
        i=i+1
    return f