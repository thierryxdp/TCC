# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que retorna uma string s, com o elemnto i substituído pelo caractere x
	tupla -> tupla"""
	
	a = len(s)
	
	if i>=0 and (i<=a):
		return s, x, x
	else:
		return s, x, i