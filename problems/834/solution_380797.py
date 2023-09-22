def media_matriz(matriz):
    """Procedimeto que recebe uma matriz de qualquer tamanho contendo apenas números inteiros e
retorna a média de todos esses números de dentro da matriz
assinatura: list --> float
casos de teste:
media_matriz([[1,1,1], [2,2,2], [1,1,1]]) == 1.33
media_matriz([[3,3,3], [2,2,2], [1,1,1]]) == 2.0
"""
    total_elementos = len(matriz)*len(matriz[0])
    soma_numeros = 0
    for l in matriz:
        soma_numeros+=sum(l)
    media = (soma_numeros)/(total_elementos)
    return round(media,2)