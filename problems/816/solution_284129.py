def maiores (lista, n):
    '''funcao que retorna uma lista com numeros maiores que n'''
    for i in lista:
        if i > n:
            lista.append(i)
            list.sort(lista)
            return [ for i in lista if i> n]