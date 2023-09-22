def inverte(frase):
    caracteres = '-,:;.!?'
    a = frase_nova.split()
    b = a[::-1]
    c = ' '.join(b)
    for c in caracteres:
        frase_nova = frase.replace(c, ' ')
	return c