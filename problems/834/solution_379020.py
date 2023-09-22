def media_matriz(lista):
    '''retorna a media de todos os numeros da matriz, list->float'''
    soma=0
    quantidade=0
    for elemento in lista:
        for matriz in elemento:
            soma=soma+matriz
            quantidade=quantidade+1
    media=soma/quantidade
    return round(media,2)