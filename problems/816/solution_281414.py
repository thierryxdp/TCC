def maiores(lista, n):
    '''Recebe uma lista e retorna uma lista com todos os inteiros maiores que n
       list, int -> list'''
    lista.sort()
    return lista[lista.index(n)-1 if n in lista else len(lista):]