def inverte(frase):
	'''funcao que dada uma frase, retorna uma outra frase que contém as mesmas palavras
palavras da frase de entrada na ordem inversa, sem letras maiusculas e sem pontuação.
string-->string'''
	g=frase
	x = str.replace(g, ('-'), ' ')
	y = str.replace(x, (','), ' ')
	z = str.replace(y, (':'), ' ')
	w = str.replace(z, (';'), ' ')
	r = str.replace(w, ('.'), ' ')
	s = str.replace(r, ('!'), ' ')
	a = str.replace(s, ('?'), ' ')
	b = a.split()[-1::-1]
	c = ' '.join(b)
	return str.lower(c)