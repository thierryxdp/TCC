def conta_numero(numero,matriz):
    ''' '''
    contador= 0
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[coluna])):
			if numero == len(matriz[coluna]):
                contador+= 1
    return contador