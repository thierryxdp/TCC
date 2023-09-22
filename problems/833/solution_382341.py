def conta_numero (numero,matriz):
    '''Função conta quantas vezes o numero aparece na matriz. 
    int, list -> int.'''
    numeros = 0
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            if matriz [i][j] == numero:
                numeros = numeros +1
    return numeros