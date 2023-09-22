def maiores(lista, n):
    numeros = list.count(lista, n)
    if numeros > n:
        list.sort(lista)
        return lista