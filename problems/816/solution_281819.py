def maiores(lista, n):
    '''função que retorna uma lista com os inteiros maiores que n em ordem crescente; list, int -> list'''
    a = list.append(lista, n)
    b = list.sort(lista)
    if lista[0] and lista[1] and lista[2] < n:
        return lista[3:]