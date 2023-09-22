def maiores(lista, n):
    ''' Retorna a partir de uma lista e um numero inteiro n os valores maiores que n em
        ordem crescente.
        list, int -> list'''
    maiores_numeros = list()
    for i in lista:
        if i >= n:
            maiores_numeros.append(i)
    return sorted(maiores_numeros)