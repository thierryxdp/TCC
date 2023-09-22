def maiores(lista, n):

    lista.append(n)
    lista.sort()

    if n <= lista[0]:
        lista.remove(n)
        return lista

    if n >= lista[-1]:
        lista.clear()
        return lista

    while n != lista[0]:
        lista.remove(n-1)
        return lista