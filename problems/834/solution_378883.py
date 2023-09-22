def media_matriz(matriz):
    '''Função que recebe uma matriz de inteiros não vazia
    e retorna a média de todos os números da matriz. Obs: a resposta
    deve vir com 2 casas decimais. list(list)->float'''
    media=0
    qtd_numeros=0
    for linha in matriz:
        for numero in linha:
            media = media + numero
            qtd_numeros= qtd_numeros +1
    resposta=round(media/qtd_numeros,2)
    return resposta