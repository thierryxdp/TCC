def maiores(lista, n):
    numeros = list.count(lista, n)
    if n > numeros:
        list.sort(lista)
        return lista
    else:
        list.append(lista, n)
        list.sort(lista)
        return lista - lista[:n]