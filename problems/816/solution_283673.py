def maiores(lista,n):

    '''Funçao que dada uma lista e um número inteiro n,
    retorna uma lista crescente com os itens maiores que n.
    
    :param lista:list
    :param n: int
    :return: list'''
    
    num_maiores=[x if x in lista if x > n]
    list.sort(num_maiores)
    
    return num_maiores