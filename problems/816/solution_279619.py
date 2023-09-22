def maiores(lista,n):
    copiaLista=lista[:4]
    copiaLista.append(n)
    copiaLista.sort()
    i=copiaLista.index(n)
    return copiaLista[:i]