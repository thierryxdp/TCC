def retira_pontuacao(frase):
	'''Função que dada uma frase, retorna a frase sem os caracteres de pontuação.
	Entrada: string
	Saída: string'''
	frase=frase.replace('!',' ')
	frase=frase.replace('?',' ') 
	frase=frase.replace('...',' ')
	frase=frase.replace('.',' ')
	frase=frase.replace(',',' ')
	frase=frase.replace('—',' ')
	frase=frase.replace(':',' ')
	frase=frase.replace(';',' ')
	frase=frase.strip()
	return frase