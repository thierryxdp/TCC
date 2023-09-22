# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
	str1 = s[0:i]
	str2 = s[i:len(s)]
    return str1 + x + str2