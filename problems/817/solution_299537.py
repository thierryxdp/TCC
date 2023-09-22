def acima_da_media(lista):
    '''recebe uma lista com notas e retorna uma lista
    com as notas acima da média. considerando media 7
    [float]->[float]'''
    media = int(sum(lista)/len(lista))
    resultado = maiores(lista,media)
    if (media in lista) and (media == resultado[0]):
        return resultado[1:]
    else:
        return resultado