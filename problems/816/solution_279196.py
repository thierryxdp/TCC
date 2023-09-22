def maiores(lista, n):
    numeros = list.count(lista, n)
    if n > numeros:
        list.sort(lista)
        return lista
    else:
        list.sort(lista)
        return lista[n:]