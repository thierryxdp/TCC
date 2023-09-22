def uppCons(frase):
	'''Função que dada uma frase, retorna a mesma com todas as consoantes em
	caixa alta.
	Entrada: string
	Saída: string'''
	frase=list(frase)
	i=0
	while i<len(frase):
		if frase[i] in 'bcçdfghjklmnpqrstvwxyz':
			frase[i]=str.upper(frase[i])
		i=i+1
	return str.join('',frase)