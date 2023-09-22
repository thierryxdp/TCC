def posLetra(frase, letra, n):
    pos = frase.find(letra)
	while pos >= 0 and n > 1:
        pos = frase.find(letra, pos + 1)
	    n -= 1
	return pos