def inverte(frase):
    caracteres = '-,:;.!?'
    for c in caracteres:
        frase_nova = frase.replace(c, ' ')
	a = frase_nova.split()
    d = a.lower()
    b = a[::-1]
    c = ' '.join(b)
    return c