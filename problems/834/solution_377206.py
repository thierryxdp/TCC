def media_matriz(matriz):
    '''função que, dada uma matriz de inteiros não vazia, retorna a média 
    de todos os números da matriz (com duas casas decimais de precisão). 
    list -> int'''
    linhas = len(matriz)
    colunas = len(matriz[0])
    quantos_elementos = linhas*colunas
    soma = 0
    
     
    for i in range(linhas):
        for j in range(colunas): 
            soma += int(matriz[i][j])
            
    media = soma/quantos_elementos
           
    return round(media,2)