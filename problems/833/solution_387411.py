'''
	
'''
def conta_numero(numero ,matriz):
    contador = 0
    i = 0
    j = 0
    while i < len(matriz):
        j = 0
        while j < len(matriz[i]):
            if matriz[i][j] == numero:
                contador += 1
            j += 1
        i += 1
    return contador