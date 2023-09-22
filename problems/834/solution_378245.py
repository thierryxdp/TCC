def media_matriz(matriz):
    ''' função que calcula a media dos valores de uma matriz'''
    
    soma = 0
    
    for lista in matriz:
        for i in lista:
            
            soma += i
            
            media = soma/(len(matriz)*len(matriz[0]))
            
    return media