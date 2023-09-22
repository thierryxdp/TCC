def media_matriz(matriz):
    """Procedimeto que recebe uma matriz de qualquer tamanho contendo apenas números inteiros e
retorna a média de todos esses números dentro da matriz
assinatura: list --> float
casos de teste:
media_matriz([[1,1,1], [1,1,1], [1,1,1]]) == 0.33
media_matriz([[3,3,3], [3,3,3], [3,3,3]]) == 1.0
"""
    total_elementos = len(matriz)*len(matriz[0])
    soma_numeros = 0
    for l in matriz:
        soma_numeros+=sum(l)
    media = (soma_numeros)/(total_elementos)
    return round(media,2)