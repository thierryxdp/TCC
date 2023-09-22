def substitui(s,x,i):
	'''Função que retorna uma string que substituí um elemento da posição i por um caractere'''
	nova_string =s[0:i] +x+ s[i+1:]
	return nova_string