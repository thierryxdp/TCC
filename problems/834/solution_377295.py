def media_matriz(lista):
    '''A função retornará a média aritmética dos números de uma matriz
    Dados de entrada -> list
    Dados de saída -> float'''
    
    nlinha = len(lista)
    ncoluna = len(lista[0])
    somador = 0
    contador = 0
    
    for i in nlinha:
        for j in lista[i]:
            contador += 1
            soma += j
            
    media = soma/contador
    return media