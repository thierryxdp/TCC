def filtraMultiplos(lista:list, n:int)->list:
    count = 0
    L = []
    while count < len(L):
        if lista[count] % n == 0:
            L.append(lista[count])
            count += 1
    return L