def media_matriz(matriz):
    ''' Dada uma matriz de inteiros nao vazia, a funcao retorna a media entre
    os seus elementos com uma precisao de duas casas decimais; 
    list -> float '''
    
    soma = 0 
    nLinhas = len(matriz)
    nColunas = len(matriz[0])
    
    for i in range(nLinhas):
        for j in range(nColunas): 
            soma = soma + matriz[i][j] 
            
    nElementos = nLinhas * nColunas 
    media = round(soma/nElementos, 2)
    
    return media