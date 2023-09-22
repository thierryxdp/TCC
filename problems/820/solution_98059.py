def posLetra(frase,letra,num):
    """..."""
    pos=0
    i=0
    while i<len(frase):
        if frase.count(letra) < num:
            pos = -1
		elif frase.count(letra) >= num:
            pos = len(frase[:i])
        i+=1
	return pos