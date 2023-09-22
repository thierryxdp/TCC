# string, int, int -> string
def substitui(s,x,i):
	'''Função que substitui um caractere da string por outro a sua escolha.'''
    return s[0:i]+x+s[i+1:]