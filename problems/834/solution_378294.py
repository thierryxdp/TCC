def media_matriz(matriz):
    '''função que recebe como entrada uma matriz não-vazia, em lista, de
    números inteiros e retorna a média de todos os números da matriz, com
    precisão de duas casas decimais; list(list)->float'''
    
    soma=0
    tamanho= len(matriz)*len(matriz[0])
    
    
    for linha in matriz:
        for elemento in linha:
            soma+=elemento
    
    
    return round((soma/tamanho),2)