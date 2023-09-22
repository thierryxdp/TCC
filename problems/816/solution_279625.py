def maiores(lista,n):
    copialista=lista[:]
    copialista.append(n)
    copialista.sort()
    copialista.append()
    i=copialista.index(n)
    return copialista[:i]