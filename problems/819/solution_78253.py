def filtraMultiplos(lista,n):
    multiploN = []
    i = 0
    while i< len(lista):
        if lista[i] % n == 0:
            multiploN.append(lista[i])
    	i = i + 1
    return multiploN