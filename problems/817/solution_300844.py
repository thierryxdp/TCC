def acima_da_media(lista):
    '''
    Funçao que recebe uma lista e retorna outra lista
    com os numeros que estao acima da media da lista
    list -> list
    '''
    m=sum(lista)/len(lista)
    list.sort(lista)
    del lista[0:list.index(lista,m)+1]
    return lista