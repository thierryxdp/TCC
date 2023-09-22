def retira_pontuacao(frase):
    caracteres = '-,:;.!?'
    for c in caracteres:
        frase = frase.replace(c, ' ')
	a = frase.split()
    b = a[::-1]
    c = ' '.join(b)
    return c