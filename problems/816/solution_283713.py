def maiores(lista,n):
    '''funcao que dada uma lista com numeros int e um
    numero n int retorna outra lista com todos os numeros
    maiores que n ordenados em ordem crescente'''
    ''' int, int -> int'''
    maiores = list()
    lista.sort()
    for a in lista:
        if a >= n:
            maiores.append(a)
    return maiores