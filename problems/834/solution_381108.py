def media_matriz(matriz):
    '''Funçao que calcula a media dos numeros de uma matriz;
    Recebe uma matriz;
    Retorna a media da matriz.'''
    a = len (matriz)
    contador = 0
    for elemento in matriz:
        b = len(elemento)
        contador += sum(elemento)
        media = (contador*1.0)/(a*b)
    return round(media, 2)