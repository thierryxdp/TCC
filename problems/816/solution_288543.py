def maiores(lista,n):
    list.sort(lista)
    for numero in lista:
        if n<numero:
            return lista[numero:]