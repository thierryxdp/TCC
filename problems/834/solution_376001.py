def media_matriz(matriz):
    '''função que dada uma matriz de inteiros não vazia, retorna a média de
    todos os números da matriz com duas casas decimais de precisão;
    list(list) -> float'''
    conta = 0
    for linha in matriz:
        for elemento in linha:
            conta = conta + elemento
    total = len(matriz)*len(matriz[0])
    media = conta/total
    return round(media,2)