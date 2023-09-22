def media_matriz(matriz):
    '''Função que recebe uma matriz de inteiros não vazia como entrada
    e retorna a média de todos os números da matriz (com duas casas
    decimais de precisão). list(list)->float'''
    soma=0
    qtd_numeros=0
    for linha in matriz:
        for numero in linha:
            soma+= numero
            qtd_numeros+=1
    media= round(soma/qtd_numeros,2)
    return media