def posLetra(frase, letra, num):
	i = 0
	while i < len(frase):
		if frase[i] == letra:
			pos = i
		i = i + 1
        if frase[i] < num:
            return -1
	return pos