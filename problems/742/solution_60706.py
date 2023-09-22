# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    loc=s.index(s[i])
	return str.replace(s,s[loc],x,1)