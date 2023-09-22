# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Funcao que recebe uma string s, um caractere x e um inteiro i entre 0 e o comprimento da string,
    e retorna uma string igual a s substituindo o elemento da posicao i pelo caractere x.
    str, str, int -> str"""
    return s[:i] + x + s[i+1:]