def maiores(n,lista):
    copiaLista=lista[:]
    copiaLista.append(n)
    copiaLista.sort()
    copiaLista.reverse()
    i=copiaLista.index(n)
    return copiaLista[:i]