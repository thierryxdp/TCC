# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    if i>=0 and i<=(len(s)-1):
        i++
    	return s[0:i] + x + s[i:]
    else:
        return "valor inválido para i"