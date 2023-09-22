def conta_numero(numero, matriz):
    ''' dado um numero inteiro e uma matriz qualquer contendo apenas inteiros
    retorna quantas vezes o numero aparece ao longo da matriz
    int, list(list) --> int '''
    
    i=0
    x = len(matriz[i])    
    while i < x-1:
        i += 1
    
    return i