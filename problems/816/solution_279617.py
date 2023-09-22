def maiores(lista,n):
    copiaLista=lista[:4]
    copiaLista.append(lista)
    copiaLista.sort()
    copiaLista.reverse()
    return copiaLista[:+1]