def inverte(frase):
	x = str.replace(frase, ('-'), ' ')
	y = str.replace(x, (','), ' ')
	z = str.replace(y, (':'), ' ')
	w = str.replace(z, (';'), ' ')
	r = str.replace(w, ('.'), ' ')
	s = str.replace(r, ('!'), ' ')
	a = str.replace(s, ('?'), ' ')
	b = a.split()
	c = ' '.join(b)
    string=c[-6:], c[0:-6]
    return string