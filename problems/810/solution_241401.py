def inverte(frase):
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
	return c