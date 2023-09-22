def eh_quadrada (lista):
    '''Funcao que identifica se a matriz é quadrada.
    list->bool'''
    
    matriz = []
    
    for i in range (lista):
        linha = []
        
        for j in range (lista):
            elemento = 0
            linha.append(elemento)
        matriz.append(linha)
    return matriz