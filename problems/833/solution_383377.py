def conta_numero(numero,matriz):
    '''Dado um número e uma matriz, retorna a quantidade de vezes que esse está presente nela. int,list-> int.'''
    contador = 0
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[i])):
            if matriz[i][j] == numero:
                contador += 1
    return contador