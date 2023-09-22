def conta_numero(numero,matriz):
    ''''''
    contador=[]
    for i in range(0,len(matriz)):
        if matriz[i]==numero:
        			contador=contador+matriz[i]
        for j in range(0,len(matriz[i])):
                    if matriz[i][j]==numero:
                    contador=contador+matriz[i][j]
    return len(contador)