def maiores(lista,n):
    copialista=lista[:]
    copialista.append(n)
    copialista.sort()
    copialista.seq.append()
    i=copialista.index(n)
    return copialista[:i]