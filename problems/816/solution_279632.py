def maiores(lista,n):
    copialista=lista[:]
    copialista.append(n)
    copialista.sort(key=int)
    copialista.reverse()
    i=copialista.index(n)
    return copialista[:i:]