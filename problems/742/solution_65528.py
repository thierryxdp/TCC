# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """
    Função que recebe uma string s, um caractere x e um numero inteiro i
    entre 0 e o comprimento da string s, e retorna uma string igual a s,
    exceto que o elemento da posição i deve ser substituído pelo
    caractere x
    str, str, int -> str
    """
    p=s[:i]+x+s[i+1:]
    return p