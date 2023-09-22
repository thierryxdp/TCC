#Questao 6
def maiores(lista, n):
    '''
    que dada uma lista de números inteiros e um número inteiro n, 
    retorna outra lista, que contenha todos os números da lista 
    original maiores que n, ordenados em ordem crescente
    str -> int
    '''
    list.append(lista, n)
    list.sort(lista)
    for i in lista:
        if i > n:
            lista.append(i)
            list.sort(lista)
    return lista