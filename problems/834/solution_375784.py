def media_matriz(matriz):
    '''Retorna a média de todos os elementos da matriz com duas casas de precisão;
    list -> float'''
    soma=0
    for linha in matriz:
        soma=soma+sum(linha)
    qtd=len(matriz)*len(matriz[0])
    return round(soma/qtd,2)