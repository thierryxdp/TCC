def filtraMultiplos(lista,N):
    elementos=[]
    for x in lista:
        if x % N == 0:
            elementos.append(x)
    return elementos