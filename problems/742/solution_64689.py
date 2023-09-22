# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    w = len (s)
    d= i-1
    f= i+1
    return s[0:i]+x+s[f:w]