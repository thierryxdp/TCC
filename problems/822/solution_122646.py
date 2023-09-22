def repetidos (lista):
    '''Retorna a quantidade de elementos iguais aos anteriores dentro da lista.
    list -> int'''
    n = 0
    contador  = 0
    while n<len(lista):
        if lista[n] == lista[(n-1)]:
            contador = contador + 1
        n  = n + 1
    return contador