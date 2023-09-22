def maiores(lista,n):
    copiaLista=lista[:i]
    copiaLista.append(n)
    copiaLista.sort()
    copiaLista.reverse()
    i=copiaLista.index(n)
    return copiaLista[:i]