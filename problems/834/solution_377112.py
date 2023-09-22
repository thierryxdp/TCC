def media_matriz(matriz):
    """Recebe uma matriz de inteiros não vazia e retorna a
       média de todos os elementos da matriz
       parâmetros de entrada:list(list)
       parâmetros de saída:float"""
    soma=0
    for aij in matriz:
        soma=soma+sum(aij)
    media=soma/(len(matriz)*len(matriz[0]))
    return round(media,2)