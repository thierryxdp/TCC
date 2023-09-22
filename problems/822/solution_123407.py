def repetidos(listadenumeros):
	sequenciais=list(zip(listadenumeros,listadenumeros[1:]))
	numerosrepetidos=[numeros[0] for (numeros in sequenciais and if numeros[0]==numeros[1])]
	return(len(numerosrepetidos))