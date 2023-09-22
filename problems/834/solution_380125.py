def media_matriz(matriz):
    '''Funçao que retorna a media dos números
    de uma matriz'''
    'list ----> float'
    c=0
    somatorio=0
    n=len(matriz)
    for  i  in  matriz:
        for j in i:
            somatorio += j
            c +=1
            media_m=somatorio%c
            return round(media, 2)