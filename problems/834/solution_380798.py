def media_matriz(matriz):
    """ função que dada uma matriz de números inteiros
    não vazia retorna a média desses números.
assinatura: list --> float
casos de teste:
media_matriz([[1,1,1], [1,1,1], [1,1,1]]) == 1.0
media_matriz([[4,4,4], [4,4,4], [4,4,4]]) == 4.0
"""
    total_elementos = len(matriz)*len(matriz[0])
    soma_numeros = 0
    for l in matriz:
        soma_numeros+=sum(l)
    media = (soma_numeros)/(total_elementos)
    return round(media,2)