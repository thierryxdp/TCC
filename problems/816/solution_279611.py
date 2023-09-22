def maiores(lista,n):
    copiaLista=lista[:]
    copiaLista.append(n)
    copiaLista.reverse()
    copiaLista.sort()
    i=copiaLista.index(n)
    return copiaLista[:i]