def maiores(lista, n):
    ''' funcao que retorna uma lista 
    com numeros maiores que n'''
    for i in lista:
        if i > n:
            list.append(n)
            list.sort(lista)
        return [i for i in lista if i> n]