def maiores(lista_int,n):
    '''
    dado uma lista de numeros inteiros e um inteiro n
    retorna uma lista contendo todos os inteiros maiores
    que n de forma ordenada(crescente)
    dados de entrada:list, int
    retorna: list
    '''
    list.append(lista_int,n)
    list.sort(lista_int)
    list.reverse(lista_int)
    m = list.index(lista_int,n)
    maiores = lista_int[:m]
    list.reverse(maiores)
    return maiores
def acima_da_media(lista_notas):
    '''
    dada uma lista de notas como entrada, retorna uma lista
    contendo todas as notas maiores que a media de forma
    ordenada(crescente)
    dados de entrada: list
    retorna: list
    '''
    media = sum(lista_notas)/len(lista_notas)
    notas_acima_media = maiores(lista_notas,media)
    return notas_acima_media