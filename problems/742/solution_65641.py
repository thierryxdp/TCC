# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """ Função que retorna uma string igual a um string s, caractere x, posição i """
	s = list(s)
	s[i] = str(x)
	s = "".join(s)
	return s