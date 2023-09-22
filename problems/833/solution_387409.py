def conta_numero(numero, matriz):
    '''Essa função tem como objetivo buscar quantas vezes um número aparece
    em uma matriz'''
    '''int, list(list) -> int'''
    
    final = 0
    if matriz == []:        
        return final
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == numero:
                final = final + 1
            
    return final