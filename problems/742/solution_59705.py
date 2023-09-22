# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
	i = len(s)-1
    	if i > 0:
       	 return s[:i]+x+s[i+1:]