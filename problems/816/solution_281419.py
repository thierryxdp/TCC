def maiores(lista, n):
    '''Recebe uma lista e retorna uma lista com todos os inteiros maiores que n
       list, int -> list'''
    lista.append(n)
    lista.sort()
    return lista[lista.index(n)+1:]