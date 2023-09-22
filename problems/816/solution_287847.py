def maiores (lista, n):
    list.sort(lista)
    valor = int(lista.index(n))
    return lista[valor:]