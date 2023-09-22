def inverte(frase):
	"""dada uma frase, retorna uma frase modificada
	str->str,str"""
	x=str.replace(frase)
	y=str.lower(x)
	z=str.split(y)
	w=list.reverse(z)
	v=str.join("",w)
	return