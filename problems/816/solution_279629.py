def maiores(lista,n):
    copialista=lista[:]
    copialista.append(n)
    copialista.sort(lista,key=int)
    copialista.reverse()
    i=copialista.index(n)
    return copialista[:i]