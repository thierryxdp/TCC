def conta_numero(numero,matriz):
    '''
    	Dada uma matriz e um número inteiro a função retorna
        quantas vezes o número aparece na matriz.
        int, list -> int
    '''
    total = matriz.count(numero)
    return total