def posLetra(frase,letra,num):
    """..."""
    pos=0
    x = num+1
    i=0
    while i<len(frase):
        if frase.count(letra) < num:
            pos = -1
		elif frase.count(letra) >= num:
            pos = frase.index(letra,num)
        i+=1
	return pos