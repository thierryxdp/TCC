def posLetra (string, letra, ocorrencia):
    indice = 0
    contador = 0
    while indice < len (string) and contador < ocorrencia:
        if string [indice] == letra:
            contador += 1
            if contador == ocorrencia:
        indice += 1
	return - 1