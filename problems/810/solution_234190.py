def inverte(frase):
	'''Função que dada uma frase retorne outra com as mesmas palavras em ordem inversa,
	sem as letras maiúsculas, e sem a pontuação.
	Entrada: string
	Saída: string'''
	frase=frase.lower()
	frase=frase.replace('!','')
	frase=frase.replace('?','') 
	frase=frase.replace('...','')
	frase=frase.replace('.','')
	frase=frase.replace(',','')
	frase=frase.replace('—','')
	frase=frase.replace('-',' ')
	frase=frase.replace(':','')
	frase=frase.replace(';','')
	frase=frase.split(' ')
	frase=frase[::-1]
	frase=' '.join(frase)
	return frase