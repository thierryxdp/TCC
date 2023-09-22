def media_matriz(matriz):
    '''Retorna a média de uma matriz de inteiros, com precisão de 2 casas decimais'''
 
    qts_elementos = len(matriz)*len(matriz[0])
    soma_elementos = 0   
    
    for linha in matriz:
        for Aij in matriz:
            soma_elementos+=Aij
    
    media = round(soma_elementos/qts_elementos,2)
    return media