def conta_numero(numero,matriz):
    ''''''
    contador=[]
    i=0
    for i in range(linhas):
            for j in range(colunas):
                if matriz[i][j]==numero:
        	contador=contador+matriz[i]
    	i=i+1
	return contador