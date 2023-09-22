def maiores (lista, n):
    '''funcao que retorna uma lista com numeros maiores que n'''
    for i in lista:
        if i > n:
            lista.append(lista, n)
            list.sort(lista)
        return [i for i in lista if i> n]