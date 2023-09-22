def maiores (lista, n):
    '''recebe uma lista de numeros inteiros e um numero inteiro n, retorna uma nova lista com apenas os numeros maiores que n'''
    '''list->list'''
    um = list.append(lista, n)
    list.sort(lista)
    posicao = list.index(lista, n)
    media = lista [posicao+1:]
    return media
   
def acima_da_media (notas):
    '''recebe uma lista com as notas dos alunos e retorna uma lista ordenada com as notas acima da média'''
    '''lista->lista'''
    return maiores