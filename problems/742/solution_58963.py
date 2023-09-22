# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """essa funcao dados os parametros s, um caractere x e um numero
	inteiro i entre 0 e o comprimento da string retorna s, com x na posicao i
	str, str, int -> str, str, int"""
    subst = s[:i] + x + s[i+1:]
    return subst