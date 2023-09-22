def filtraMultiplos (lista,n):
    multiplos=[]
    i=0
    
    while i<len(lista):
        if lista[i]%n==0:
            lista.append(multiplos,lista[i])
            return multiplos