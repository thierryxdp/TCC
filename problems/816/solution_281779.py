def maiores(lista,n):
    if n in lista:
        list.sort(lista)
        return lista[list.count(lista,n)+list.index(lista,n):]
    elif n not in lista:
        list.append(lista,n)
        list.sort(lista)
        return lista[list.index(lista,n)+1:-1]