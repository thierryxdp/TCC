def uppCons(frase):
	"""funcao que dada uma frase retorna essa mesma frase com todas suas consoantes em maiusculo;str->str"""
	i=0
	s=[]
	while i<len(frase):
		if frase[i]in 'bcdfghjklmnpqrstvwxyzç':
			s=s+[str.upper(frase[i])]
		else:
			s=s+[frase[i]]
		i=i+1
	return str.join('',s)