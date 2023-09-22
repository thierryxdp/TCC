def filtraMultiplos(lista,n):
    mult=[]
    i=0
    while i < len(lista):
        if lista[i]%n == 0:
            mult.insert(0,lista[i])
        i = i + 1
    return mult