def posLetra(frase, letra, num):
	i = 0
	for i in letra:
        if frase [i] == letra:
            pos = i
        else:
            pos = -i
    return pos