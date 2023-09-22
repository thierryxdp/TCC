def maiores(lista,n):
    copiaLista=lista[:4]
    copiaLista.append(n)
    copiaLista.sort()
    copiaLista.reverse()
    return copiaLista[:+1]