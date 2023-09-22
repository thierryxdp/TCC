def media_matriz(matriz):
    '''função em que dada uma matriz de inteiros não 
    vazia, retorna a média de todos os números da matriz
    (com exatamente duas casas decimais de precisão;
    list -> float'''
    x = 0
    for linha in matriz:
        for elem in linha:
            x = x + elem
        qtd = x/(len(matriz)*len(matriz[0]))
    return round(qtd, 2)