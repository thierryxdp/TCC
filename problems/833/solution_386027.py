def conta_numero(numero,matriz):
    a=0
    for i in range(len(matriz)):
         for j in range(len(matriz[0])): 
            if matriz[i][j] == numero:
                a+=1
    return a