def conta_numero(numero,matriz):
    '''
    	Dada uma matriz e um número inteiro a função retorna
        quantas vezes o número aparece na matriz.
        int, list -> int
    '''
    total = 0
    nlin = len(matriz)
    ncol = len(matriz[0])
    for i in range(nlin):
        for j in range(ncol):
            if numero in matriz:
                total = total + list.count(numero)
    return total