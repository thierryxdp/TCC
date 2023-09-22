def inverte(frase):
	x = str.replace(frase, ('-'), ' ')
	y = str.replace(x, (','), ' ')
	z = str.replace(y, (':'), ' ')
	w = str.replace(z, (';'), ' ')
	r = str.replace(w, ('.'), ' ')
	s = str.replace(r, ('!'), ' ')
	a = str.replace(s, ('?'), ' ')
	b= a.split()
	string = ' '.join(b)
	stringlength=len(string)
	slicedString=string[stringlength:-1]
	return slicedString