def conta_numero (numero, matriz):
    contador = 0 
    for i in range(len(matriz[0])):
        for j in range(len(matriz)):
            if matriz[i][j] == numero:
                contador += 1
            else: 
                pass 
    return contador