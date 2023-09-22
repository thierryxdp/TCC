def media_matriz(matriz):
    '''função quer retorna a media de todos os elementos
    da matriz.'''
    soma_elementos=0
    total=0
    for linha in matriz:
        for elem in linha:
            soma_elementos=soma_elementos+elem
            total=total+1
    return soma_elementos/total