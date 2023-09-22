def posLetra(frase, letra, num):
	for i in range(len(frase)):
		if frase [i] == letra:
			pos = i
        if frase [i] != letra:
            pos = -1
	return pos