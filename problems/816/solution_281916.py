def maiores(lista, n):
    '''função que retorna uma lista com os inteiros maiores que n em ordem crescente; list, int -> list'''
    a = list.append(lista, n)
    b = list.sort(lista)
    c = list.index(lista, n)
    lista2 = lista[c + 1:]
    return lista2