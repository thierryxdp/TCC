def posLetra(frase, letra, n):
    '''função que mostra a posição de uma letra em sua x repetição. str -> int'''
    i=0
    indicador=0
    while i < len(frase):
    	if  frase[i] in letra:
            indicador = indicador + 1
        if indicador  == n:
            return i
        elif indicador < n:
        	return -1
    	i=i+1