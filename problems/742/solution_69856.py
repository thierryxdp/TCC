# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Esta funcao recebe uma string, um numero i e um caractere, substituindo
    na saida s o caractere por x na posicao i."""
	return s[0:i-1]+str(x)+s[i+1::]