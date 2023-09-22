def conta_numero(numero,matriz):
    '''Essa função retorna quantas vezes um numero aparece em uma matriz.
    int, list >>> int '''
    
    contador = 0
    
    for i in range (len(matriz)):
        for j in range(len(matriz[i])):
            if matriz [i] == numero:
                contador += 1
               
    return contador