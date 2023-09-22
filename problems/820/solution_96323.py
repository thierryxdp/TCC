def posLetra (string, letra, ocorrencia):
    indice = 0
    contador = 0
    while indice < len (string) and contador < ocorrencia:
        if letra [indice] == ocorrencia:
            contador += 1
        indice += 1
		else:
            return -1
	return indice