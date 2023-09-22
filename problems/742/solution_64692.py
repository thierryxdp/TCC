# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """ substitui uma letra na string
    str, str, int -> str"""
    w = len (s)
    f= i+1
    return s[0:i]+x+s[f:w]