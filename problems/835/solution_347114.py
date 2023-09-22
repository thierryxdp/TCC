def melhor_volta(matriz):
    """Retorna uma tupla com o menor tempo de uma volta em uma corrida de 
    kart além de identificar o corredor e em qual volta ele teve esse melhor
    tempo
    list -> tuple
    """
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