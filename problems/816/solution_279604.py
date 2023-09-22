def maiores(lista,n):
    copiaLista=lista[:]
    copiaLista.append[n]
    copiaLista.sort()
    copiaLista.reverse()
    i=copiaLista.index(n)
    return copiaLista[:i]