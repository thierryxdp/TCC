def inverte(frase):
    caracteres = '-,:;.!?'
    for c in caracteres:
        frase1 = frase.replace(c, ' ')
	a = frase1.split()
    b = a[::-1]
    c = ' '.join(b)
    return c