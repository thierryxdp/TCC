def conta_numero(numero,matriz):
    '''conta o numero de vezes que um certo numero inteiro se repete em uma matriz
    int, list -> list'''

    repeticoes = 0
    
    for coluna in matriz:
        for elemento in coluna:
            if elemento == numero:
                repeticoes = repeticoes + 1
                
    return repeticoes