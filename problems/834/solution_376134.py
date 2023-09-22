def media_matriz(matriz):
    '''
    Calcula a média dos elementos de uma matriz.
    list -> float

    Parameters:    
    matriz: Parâmetro do tipo lista (list).

    Returns:
    A média dos elementos de uma matriz com duas casas decimais de precisão.    
    '''
    
    linhas = len(matriz)
    colunas = len(matriz[0])
    somatorio = 0
    

    for i in range(linhas):
        for j in range(colunas):
            if type(matriz[i][j]) != int:
                return ("Utilize somente valores inteiros para os elementos da matriz. Tente novamente!")
            

    quantidade_elementos = linhas * colunas
    
    for i in range(linhas):
        for j in range(colunas):
            somatorio = somatorio + matriz[i][j]

    media = round((somatorio / quantidade_elementos), 2)

    return media