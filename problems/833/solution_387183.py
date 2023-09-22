def conta_numero(numero,matriz):
    '''Função que, dado um numero inteiro e uma matriz,
     conta e retorna quantas vezes aquele numero aparece
     na matriz.
     int,list -> int
    '''
    n = 0 
    for elemento in matriz:
        for elem in elemento:
            if elemento == numero:
                n += 1
    return n