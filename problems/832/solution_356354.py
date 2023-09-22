def eh_quadrada (lista):
    '''Funcao que identifica se a matriz é quadrada.
    list->bool'''
    
    matriz = []
    
    for i in range(len(lista)):
        linha = []
        
        for j in range(len(lista)):
            elemento = i+1
            linha.append(elemento)
        matriz.append(linha)
        len(lista)==matriz
        return True