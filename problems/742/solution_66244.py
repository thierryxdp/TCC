# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string (ta errada essa analise de tipo)
def substitui(s,x,i):
	'''substitui a variavel x, na posição i, dentro da string s
    	String, String, int -> string''' 
    return s[:i] + x + s[i+1:]