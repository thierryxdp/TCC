def conta_numero(numero, matriz):
    '''percorre a matriz inteira e verifica se há numero
    int, list--> int '''

    total = 0

    for item in matriz:
        for item2 in item:
            if item2 == elemento:
                total += 1
    
    return total