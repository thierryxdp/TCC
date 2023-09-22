def maiores(lista,n):
    copiaLista=lista[:]
    copiaLista.append(n)
    copiaLista.sort()
    i=copiaLista.index(n)
    return copiaLista[:i]