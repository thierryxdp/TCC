# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ''' Substitui um elemento da string (s) na posição (i) por (x)
    str, str, int -> str'''
    return s[:i] + x + s[i:]