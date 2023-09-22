def maiores(lista_numeros, n):
    lista1 = lista_numeros
    lista2 = [n]
    if lista1 >= lista2:
        list.sort(lista1)
        return lista1
    else:
        return []