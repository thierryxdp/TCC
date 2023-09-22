def melhor_volta(matriz):
	    linha = len(matriz)
	    coluna = len(matriz[0])
	    minimo = matriz[0][0]
	    tupla = ()
	    for i in range(linha):
	        for j in range(coluna):
	            if matriz[i][j] < minimo:
	                minimo = matriz[i][j]
	                tupla = (i+1,minimo,j+1)
	    
	    return tupla