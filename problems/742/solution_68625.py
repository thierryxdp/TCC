# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, string, int -> string
def substitui(s,x,i):
	""" substitui o valor de i pelo valor  de x 
	string, string, int -> string """

	return s[:i] + str (x) + s[i+1:]