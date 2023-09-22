# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Funcao vai retornar a subistituicão de uma string(x) por um caractere(x) e um numero inteiro(i)"""
    return s[:i]+x+s[i:i+2:]