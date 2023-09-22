def media_matriz(matriz):
    '''retorna a media entre os elementos de uma matriz, com duas casas decimais de aproximacao; list -> flot'''
    contador = 0
    for linha in matriz:
        for elemento in linha:
            contador = contador + elemento
    media = contador/((len(matriz)+len(matriz[0]))
                      
    return round(media,2)