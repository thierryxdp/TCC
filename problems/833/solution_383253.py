def conta_numero(numero,matriz):
    ''''''
    contador=[]
    for i in range(0,len(matriz)):
            for j in range(0,len(matriz[i])):
                if matriz[i]==numero:
        			contador=contador+matriz[i]
	return len(contador)