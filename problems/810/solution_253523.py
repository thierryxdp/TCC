def inverte(frase):
    caracteres = '-,:;.!?'
    for c in caracteres:
        frase_nova = frase.replace(c, ' ')
	a = frase_nova.split()
    b = a[::-1]
    c = ' '.join(b)
    d = c.lower()
    return d