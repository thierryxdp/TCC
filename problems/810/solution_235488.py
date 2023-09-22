def inverte(x):
	"""Função em que dada uma frase x retorna ela ao contrário sem letra maiúsculas e pontuação.
	string -> string"""
	x=x.replace('.',' ')
	x=x.replace(',',' ')
	x=x.replace('/',' ')
	x=x.replace(':',' ')
	x=x.replace(';',' ')
	x=x.replace('!',' ')
	x=x.replace('?',' ')
	x=x.replace('-',' ')
	x=list(x.split(' '))
	x=x[::-1]
	x.join(' ')
	return x