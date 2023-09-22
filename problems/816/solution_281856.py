def maiores(lista, n):
    '''Coloque uma lista e um número n.
       O resultado será uma lista com todos os números maiores que o número n'''
    list.append(lista, n)
    list.sort(lista)
    indice=list.index(lista, n) + 1
    lista1=lista[indice::]
    return lista1