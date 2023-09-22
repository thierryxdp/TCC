def posLetra(string, letra, numero):
    pos = string.find(letra)
    if string.count(letra) >= numero:
        while pos >= 0 and numero > 1:
        	pos = string.find(letra, pos + 1)
        	numero = numero - 1
    return pos
	else:
        return -1