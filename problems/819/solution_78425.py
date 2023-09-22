def filtraMultiplos(lista,n):
    """ """
    i=0
    mult=[]

    while i < len(lista):
        if lista[i]%n==0:
            mult = mult +lista[i]
            i=i+1
        else: i=i+1
     
    return mult