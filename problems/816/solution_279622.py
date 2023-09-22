def maiores(lista,n):
    copialista=lista[:]
    copialista.append(n)
    copialista.sort()
    i=copialista.index(lista)
    return copialista[:i]