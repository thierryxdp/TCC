def filtraMultiplos(lista,n):
    c=0
    L=[]
    while c<len(lista):
         if lista[c]%n==0:
            L = L + [lista[c]]
        c=c+1
    return L