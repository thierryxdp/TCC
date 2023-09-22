def media_matriz(matriz):
    '''
    função que recebe uma matriz de inteiros não vazia
    e retorna a média de todos os números da matriz  
    list->float 
    '''
    soma = 0
    for num in range(len(matriz)):
        M = matriz[num]
        for elem in range(len(M)):
            soma = soma + M[elem]        
    return round((soma/(len(matriz)*len(matriz[0]))),2)