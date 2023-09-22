# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    b=s[0:i]+s[i:-1]
   	c=b[0:i]+"x"+b[i:-1]
   	return c