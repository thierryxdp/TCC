def maiores(lista,n):
    '''Funçao que retorna uma lista com todos os numeros em ordem crescente
    e maiores que o numero de entrada n
    list, int -> list'''
    list = lista
    list.append(n)
    list.sort()
    list = list[(list.index(n)+1):]
    return list