def filtraMultiplos(lista,n):
    ''' retorna '''
    Multiplos=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            Multiplos = Multiplos + [lista[i],]
        i = i+1
    return Multiplos