def posLetra(string, letra, o):
    indice = ocorrencia = 0
    while indice <len(string):
    	if string[indice]==letra:
    	ocorrencia+=1
    	if ocorrencia == o:
    		return string.index(string[indice],indice)
    	indice+=1
    	else:
        	return -1