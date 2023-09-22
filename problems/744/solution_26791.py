def hashtag(s):
	'''Função que recebe uma string e insere o caractere "#" no início, no meio e no final da mesma;
	Entrada: string
	Saída: string'''
	s = '#'+ s[:len(s) // 2] + '#' + s[len(s) // 2:] + '#'
	return s