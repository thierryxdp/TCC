def maiores(lista,n):
    copialista=lista[:]
    copialista.append(n)
    copialista.sort(key=int)
    copialista.reverse(key=int )
    i=copialista.index(n)
    return copialista[:i]