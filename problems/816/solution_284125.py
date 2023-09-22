def maiores(lista, n):
    '''Retorna uma lista, em ordem crescente, com os número 
    maiores que n presentes na lista dada como parâmetro (com
    números inteiros)
    list, int --> list'''
    list.append(lista, n)
    list.sort(lista)
    indice = list.index(lista, n)
    maiores = lista [indice + 1:]
    return maiores