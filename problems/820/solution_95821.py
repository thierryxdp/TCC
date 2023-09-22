def posLetra(frase, letra, num):
	for i in range(len(frase)):
		if frase [i] == letra:
			pos = i
        else:
            return -1
	return pos