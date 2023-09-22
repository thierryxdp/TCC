def filtraMultiplos(lista,n):
    L=[]
    i=0
    
    while i < len(lista):
        if lista[i] % n==0:
            i=i+1
            return lista