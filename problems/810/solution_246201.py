def invert(frase):
	"""dada uma frase, retornaa frase modificada
str->str"""
	x=retira_pontuacao(frase)
	y=str.lower(x)
	z=str.split(y)
	w=list.reverse(z)
	v=str.join("",w)
	return