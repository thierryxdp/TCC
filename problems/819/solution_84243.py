def filtraMultiplos(lista,n):
    l =[]
    indice= 0
    for i in lista:
        if lista[indice] % n == 0:
            l.append(i)
    indice+=1
    return l