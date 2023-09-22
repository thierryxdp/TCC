def posLetra(frase, letra, num):
	for i in range(len(frase)):
		if frase [i] == letra:
			pos = i
        else:
            pos = -1
	return pos