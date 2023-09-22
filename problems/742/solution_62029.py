# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """funcao que recebe uma string, um caractere e um inteiro e retorna uma string igual a s"""
    """str,int,int -> str"""
    return s[:i] + x + s[i+1:]