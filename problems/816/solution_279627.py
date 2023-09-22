def maiores(lista,n):
    copialista=lista[:]
    copialista.append(n)
    copialista.sort()
    copialista.reverse(-1)
    i=copialista.index(n)
    return copialista[:i]