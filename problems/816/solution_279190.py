def maiores(lista, n):
    numeros = list.count(lista, n)
    if numero > n:
        list.sort(lista)
        return lista
    else:
        return lista - lista[:n]