# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que retorna uma string s, com o elemento i substituído pelo caractere x
	str, str, int -> str"""
	
	a = len(s)
	
	if i>=0 and (i<=a):
		return s[0:i] + x + s[i + 1:]
	else:
		return 'Inválida'