# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """função que recebe uma string s e um caractere x e um número inteiro i, e retorna uma string igual,
	mas substituindo o elemento da posição i pelo caractere x
	string, int, int -> string"""
    
    return s[0:i] + x + s[i + 1:]