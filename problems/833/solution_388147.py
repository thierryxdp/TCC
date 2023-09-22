def conta_numero(numero,matriz):
    '''
    	Dada uma matriz e um número inteiro a função retorna
        quantas vezes o número aparece na matriz.
        int, list -> int
    '''
    total = 0
    for numero in matriz:
        total = total + list.count(matriz,numero)
    return total