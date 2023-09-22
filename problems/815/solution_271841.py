def insere(lista_numero,n):
    '''recebe uma lista ordenada crescente de números 
    inteiros e um número inteiro n, inclui n em uma
    posição de forma que continue ordenada
    [int],int->[int]'''
    list.sort(lista_numero)
    return list.insert(lista_numero,n-1,n)