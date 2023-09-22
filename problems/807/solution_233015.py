def conta_frases(texto):
	l1 = texto.split('. ', -1)
    del l1[1:]
    l2 = texto.split('! ', -1)
    l3 = texto.split('... ', -1)
    l4 = texto.split('? ', -1)
    return l1