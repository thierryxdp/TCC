def conta_numero(numero, matriz):
    '''
    Conta quantas vezes um número aparece na matriz;
    int, list -> int
    '''
    
    contador = 0
    for line in matriz:
        for valor in line:
            if valor == numero:
                contador += 1
    return contador