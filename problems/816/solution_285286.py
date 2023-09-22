def maiores(lista_numeros, n):
    lista1 = lista_numeros
    lista2 = [n]
    if lista1 > lista2:
        list.sort(lista1)
        lista = lista[list.index(lista1,lista2)+1]
        return lista
    else:
        return []