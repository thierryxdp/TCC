def media_matriz(matriz):
    '''Dada uma matriz de inteiros nao vazia, retorna a media de 
    todos os numeros da matriz(com duas casas decimais de precisao).
    list -> int'''
    i=0
    media=0
    while i<len(matriz):
        media=media+((sum(matriz[i]))/len(matriz[i]))
        i=i+1
    return round(media/i,2)