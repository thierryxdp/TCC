def conta_numero(numero,matriz):
    ''''''
    contador=[]
    for i in range(0,len(matriz)):
        if matriz[i]==numero:
        			contador=contador+matriz[i]
        for j in range(0,len(matriz[i])):
                    if matriz[j]==numero:
        		contador=contador+matriz[i]
    return len(contador)