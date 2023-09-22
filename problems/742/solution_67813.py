# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """retorna uma string s, igual a s onde o elemento na posição i é igual a x. (str,var,int->str)"""
    if i<=int(len(s)):
	s[i]=x
	return str(s)