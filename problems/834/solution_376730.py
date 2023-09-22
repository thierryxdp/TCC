def media_matriz(matriz):
    '''Funcao que dada uma matriz
    de inteiros nao vazios, retorna
    a media aritimetica de todos os
    numeros da matriz.
    Dados de entrada: list[list] 
    Valor de saida: float
    '''
    soma_elementos = 0
    qtd_elementos = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma_elementos += matriz[i][j]
            qtd_elementos += 1 
        media = (soma_elementos/qtd_elementos)
    return round(media,2)