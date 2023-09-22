def melhor_volta(matriz):

 	tupla = (0,float('inf'),0)

 	for x in range(6):

   	for y in range(10):

     	if matriz[x][y] < tupla[1]:

       	tupla = (x+1,matriz[x][y],y+1) 

 	return tupla