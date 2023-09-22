def media_matriz(matriz):
    '''Dada uma matriz de inteiros nao vazia,
       a funcao retorna a média de todos os 
       numeros da matriz;
       list -> float'''
    soma = 0
    ndeelementos=0
    i=0
    while i < len(matriz):
        for elemento in matriz[i]:
            ndeelementos= 1 + ndeelementos
            soma = elemento + soma 
        i = i + 1
    return round(soma/ndeelementos,2)