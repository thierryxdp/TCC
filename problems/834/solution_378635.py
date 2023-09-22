def media_matriz(matriz):
    '''Dada uma matriz de inteiros não vazia, retorna a média de todos
       os números da matriz (com duas casas decimais);
       list -> float'''
    soma = 0 
    total_de_numeros = len(matriz)*len(matriz[0])
    for linha in matriz:
        for aij in linha:
            soma = soma + aij
    return round(soma/total_de_numeros, 2)