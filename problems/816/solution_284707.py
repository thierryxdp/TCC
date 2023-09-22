#Questao 6
def maiores(lista, n):
    '''
    que dada uma lista de números inteiros e um número inteiro n, 
    retorna outra lista, que contenha todos os números da lista 
    original maiores que n, ordenados em ordem crescente
    str -> int
    '''
    lista1=[]
    for b in lista:
        if b > n:
            lista1.append(b)
            list.sort(lista1)
    return lista1