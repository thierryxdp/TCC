def maiores(lista,n):
    copialista=lista[:]
    copialista.append(n)
    copialista.sort(key=int,reverse=True)
    copialista.reverse()
    i=copialista.index(n)
    return copialista[:i]