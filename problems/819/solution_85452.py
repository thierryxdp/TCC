def filtraMultiplos(listnumeros,n):
    Multiplos=[]
    i=0
    while i<len(listnumeros):
        if listnumeros[i]%n == 0:
            Multiplos=Multiplos+[listnumeros[i],]
        i=i+1
    return Multiplos