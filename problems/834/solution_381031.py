def media_matriz(matriz):
    """funcao que dada uma matriz de inteiros nao vazia, 
    retorna a media de todos os numeros da matriz com duas
    casas decimais de precisao
    list->float"""
    soma = 0
    for x in range(len(matriz)):
        soma = soma + sum(matriz[x])
    return round(soma/(len(matriz)*len(matriz[0])),2)