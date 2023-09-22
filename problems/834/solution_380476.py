def media_matriz(M):
    '''
    funcao que recebe uma matriz M de inteiros nao vazia
    e retorna a media de todos os numeros dessa matriz,
    com duas casas decimais
    list->float
    '''
    somatorio=0
    items_matriz=0
    if M!=[]:
        for m in range(0, len(M)):
            for n in range(0,len(M[m])):
                items_matriz=items_matriz+1
                somatorio=somatorio+M[m][n]
                media=somatorio/items_matriz
    return round(media,2)