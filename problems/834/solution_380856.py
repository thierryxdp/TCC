def media_matriz(matriz):
    '''Dada uma matriz de números inteiros não vazia,
    a função retorna a média de todos os numeros da
    matriz com precisão de duas casas decimais. 
    list --> float'''
    
    #número de elementos de uma matriz:
    #linhas*colunas
    #len(matriz)*len(matriz[0]), se houver mais de 1 coluna
    
    if len(matriz[0])==1:
        media=sum(matriz)/len(matriz)
            
    if len(matriz[0])>1:
        media=sum(matriz)/(len(matriz)*len(matriz[0]))
                               
    return media