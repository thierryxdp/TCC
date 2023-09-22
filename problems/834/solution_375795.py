def media_matriz(matriz):
    '''A partir de uma matriz;
retorna a média de todos os números da matriz com precisão de 2 casas;
list => float'''
    if len(matriz)==0:
        return 0
    else:
        soma = 0
        x = len(matriz)*len(matriz[0])
        for linha in matriz:
            for elemento in linha:
                soma = soma+elemento
        return round(soma/x,2)