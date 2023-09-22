# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
	antes= s[0:2]
    adicionar= str(x)
    depois= s[i:lens(s)]
    return antes + adicionar + depois