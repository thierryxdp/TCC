# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que recebe uma string, um caractere x e um numero e retorna uma sting"""
    s[i] = x
    return s
	return s[0:i] + x + s[i+1:]