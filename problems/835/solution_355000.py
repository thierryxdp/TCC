def melhor_volta(matriz):

	lista_tempos = []
	lista_voltas = []
    

	for voltas in range(6):
		for tempos in range(10):
			if matriz[voltas][tempos] == min(matriz[voltas]):
				lista_tempos.append(tempos)
                
	for i in range(6):
		lista_voltas.append(matriz[i][lista_tempos[i]])
        
	volta = lista_voltas.index(min(lista_voltas))
	tempo = min(lista_voltas)
	piloto = matriz[volta].index(tempo) + 1
    
	tupla = (volta + 1, tempo, piloto)
    
	return tupla