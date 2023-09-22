def conta_numero(numero, matriz):
    '''
    	essa função recebe um número e uma matriz e retorna a quantidade de vezes que esse
        determinado número aparece na matriz dada.
        num, list -> num
    '''
    a = []
    nLinha = len(matriz)
    for i in range(nLinha):
        if matriz[i] == numero:
            a.append(i)
    return a