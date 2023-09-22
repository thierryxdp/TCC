def media_matriz(matriz):
    '''dada uma matriz de inteiros não vazia, retorna a média de todos os números da matriz com duas casas decimais de precisão;
    list --> float'''
    numerador=0
    denominador=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            numerador+=matriz[i][j]
            denominador+=1
    media=numerador/denominador
    return round(media,2)