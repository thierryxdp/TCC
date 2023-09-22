# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    s = len(s)
    s[i] = x
    s = tuple(s)
    return tuple(s)