def posLetra(frase, letra, num):
	i = 0
    i = i + 1
	while i < len(frase):
		if frase[i] == letra:
			pos = i
        if frase[i] != letra:
            pos = -1
    return pos