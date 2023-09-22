def conta_numero(numero, matriz):
    
    ''' Função que, dado um numero inteiro
        e uma matriz de inteiros, conta quantas 
        vezes o numero aparece na matriz.
        int, list -> int '''
    
    contador = 0
    
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            if numero == matriz[l][c]:
                contador += 1
    
    return contador