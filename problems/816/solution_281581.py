def maiores(lista,n):
    '''
    Função que recebe uma lista e um número inteiro n e
    retorna outra lista que contém todos os numeros da lista 
    original maiores que n em ordem crescente.
    
    list->list
    '''
    a=list(range(n,-1))
    a.sort()
    return a