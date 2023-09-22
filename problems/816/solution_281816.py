def maiores(lista, n):
    '''função que retorna uma lista com os inteiros maiores que n em ordem crescente; list, int -> list'''
    a = list.append(lista, n)
    b = list.sort(lista)
    k = lista[1:]
    if lista[0] < n:
        return k