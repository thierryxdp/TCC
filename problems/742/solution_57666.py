# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
	'''
	Substitui em uma string s o caracter no index i pelo caracter <x>
	'''
	ini_string = s[:i]
	fim_string = s[i+1:]
    
	return ini_string + x + fim_string