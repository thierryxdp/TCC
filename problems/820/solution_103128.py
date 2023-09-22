def posLetra(frase, letra, n):
    '''função que mostra a posição de uma letra em sua x repetição. str -> int'''
    i=0
    indicador=0
    while i < len(frase):
    	if  frase[i] == letra:
            indicador = indicador + 1
    	i=i+1