def maiores(lista,n):
    copialista=lista[:]
    copialista.append(n)
    copialista.sort()
    i=copialista.index(n)
    return copialista[:i]