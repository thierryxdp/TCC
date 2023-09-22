def maiores (lista,n):
    '''Retorna os números da lista maiores que n, list, int -> list'''
    lista = list (filter(lambda x: x>n, lista))
    return sorted (lista)

def acima_da_media (lista):
    ''' Diz quais notas ficaram acima da média entre elas, list -> list'''
    n = sum (lista) / len (lista)
    return n