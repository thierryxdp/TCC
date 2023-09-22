# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Recebe uma string s, um caractere x e um inteiro i entre 0 e o comprimento da string.
    Retorna uma string igual a s em que o elemento na posição i é substituído pelo caractere x."""
    if i>len(s):
    	return 'i é maior que o número de caracteres de s, tente de novo!'
	elif i>=len(s):
		l=len(s)
        resposta=s[0:i-1]+'x'+[i+1:l]