def conta_numero(numero, matriz):
    '''A seguinte função percorre toda a matriz 
    inteira e irá ver se há número
    int, list--> int'''

    total = 0

    for elemento in matriz:
        for elemento_2 in elemento:
            if elemento_2 == numero: 
                total += 1 
    
    return total