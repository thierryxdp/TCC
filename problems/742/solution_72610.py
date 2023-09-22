# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Retorne uma string igual a s, exceto que o elemento da posicao i deve ser 
    substitudo pelo caractere x;
    string, int, int -> string"""
	if i >= 0 and i < len(s):
    	return s[0:i] + str(x) + s[i+1:]