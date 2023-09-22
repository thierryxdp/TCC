def posLetra(string, letra, indicador=0):

	if (string.count(letra) >= indicador):
        lista = list(string)
    	for indice in range(indicador-1):
            numb = int(lista.index(letra))
        	lista[numb] = " "
        string = "".join(lista)
        return string.index(letra)
	return -1