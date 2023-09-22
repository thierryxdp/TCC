def inverte(frase):
    g=frase[-1::-1]
	x = str.replace(g, ('-'), ' ')
	y = str.replace(x, (','), ' ')
	z = str.replace(y, (':'), ' ')
	w = str.replace(z, (';'), ' ')
	r = str.replace(w, ('.'), ' ')
	s = str.replace(r, ('!'), ' ')
	a = str.replace(s, ('?'), ' ')
	b = a.split()
	c = ' '.join(b)
	return c