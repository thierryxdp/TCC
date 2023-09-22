def eh_quadrada (lista):
    '''Funcao que identifica se a matriz é quadrada.
    list->bool'''
    
    matriz = []
    
    for i in (lista+1):
        linha = []
        
        for j in (lista+1):
            elemento = 0
            linha.append(elemento)
        matriz.append(linha)
    return matriz