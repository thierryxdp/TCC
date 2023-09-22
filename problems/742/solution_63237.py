# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """A função substitui e retorna uma string igual a s,
    substituindo o elemento na posição i pelo caractere x;
	str, str, int -> str"""
    s[i] = str(x)
    return s