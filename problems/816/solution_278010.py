def maiores(lista,n):
    if min(lista)>n:
        list.sort(lista)
        return lista
    if max(lista)<n:
        list.append(lista,n)
        list.sort(lista)
        return lista[n:]