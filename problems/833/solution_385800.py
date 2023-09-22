def conta_numeros(numero, matriz):
    '''
    	essa função recebe um número e uma matriz e retorna a quantidade de vezes que esse
        determinado número aparece na matriz dada.
        num, list -> num
    '''
    nLinha = len(matriz)
    nColuna = len(matriz[0])
    for i in range(nLinha):
        for j in range(noluna):
            if numero in matriz:
                return list.count(matriz,numero)
            else:
                return 0