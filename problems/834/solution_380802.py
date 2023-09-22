def media_matriz(matriz):
    '''Função que dada uma matriz de inteiros não vazia, 
    retorna a média de todos os números da matriz.
    assinatura: list -> float '''
    elementos = len(matriz)*len(matriz[0])
    soma = 0
    for i in matriz:
        soma += sum(i)
    media = (soma)/(elementos)
    return round(media, 2)