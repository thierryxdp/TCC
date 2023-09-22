# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
	'''função que subistitui uma letra de uma palavra de acordo com a ordem escolhida'''
	'''string,string,int -> string'''
	return str(s[:i]) + x + (s[(i+1):])