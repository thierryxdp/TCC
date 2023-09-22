def conta_numero(numero,matriz):
    '''
    	Dada uma matriz e um número inteiro a função retorna
        quantas vezes o número aparece na matriz.
        int, list -> int
    '''
    total = 0
    for i in matriz:
        if i == numero:
            total += 1
    return total