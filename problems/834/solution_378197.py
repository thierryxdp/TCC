def media_matriz(matriz):
    ''' Função que dada uma matriz de números inteiros não
    vazia, retorna a media de todos os números da matriz.
    Entrada: list
    Retorno: float '''
    
    soma_elementos = 0
    qtd_elementos = 0
    for i in matriz:
        soma_elementos += sum(i)
        qtd_elementos += len(i)
    media = soma_elementos/qtd_elementos
    return round(media,2)