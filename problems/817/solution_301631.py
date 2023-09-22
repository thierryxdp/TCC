def acima_da_media(lista):
    '''Recebe uma lista de notas (lista), e retorna
    uma lista ordenada com as notas que ficaram
    acima da media
    
    list -> list
    '''
    media = int(sum(lista)/len(lista))
    
    return maiores(lista, media)