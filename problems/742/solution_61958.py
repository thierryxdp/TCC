# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Funcao que recebe uma string s, um caractere x e um número inteiro i entre 0 e o comprimento da string, e retorne uma string igual a s, exceto que o elemento da posição i deve ser substituido pelo caractere x,
    str, int, int -> str"""
    return s[:i] + x + s[i+1:]