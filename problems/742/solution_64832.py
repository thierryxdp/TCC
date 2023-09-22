# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''s -> string
    x -> string
    i -> int'''
    y = i + 1
    return s[0 : i] + x + s[y:]