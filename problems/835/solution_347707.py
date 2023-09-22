def melhor_volta(matriz):
    """Dada uma matriz 6x10 com tempos em seg, retorna uma
tupla que contém nome, tempo e volta do melhor colocado.
list -> tuple"""
 	tupla = (0,float('inf'),0)
 	for i in range(6):
   		for j in range(10):
			if matriz[i][j] < tupla[1]:
       			tupla = (i+1,matriz[i][j],j+1)
 	return tupla