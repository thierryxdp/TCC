# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Retorna uma string igual a s com a modificação feita por i
    str, str, int -> str'''
ns = s[0:i] + x + s[i+1:]
	return ns