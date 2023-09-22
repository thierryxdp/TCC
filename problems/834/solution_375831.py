def media_matriz(matriz):
    '''retorna a media de todos os numeros da matriz de numeros inteiros e nao vazia 
    dada, com duas casas decimais de precisao
    list-->float'''
    soma=0
    for i in matriz:
        soma+=sum(i)
    return round(soma/(len(matriz)*len(matriz[0])),2)