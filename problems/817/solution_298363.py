def maiores(lista,n):
    '''Dado uma lista, a fução retorna os valores
    maiores que n em ordem list->list'''
    x = ([i for i in lista if i > n])
    return sorted(x)
    
def acima_da_media(lista1):
    '''Dada uma lista, a funcao retornara na ordem
    os valores que sejam maiores q a média da lista
    list->list'''
    c = sum(lista1)/len(lista1)
    return maiores(lista1,c)