# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ""
    lim = len(s)
    if lim >= i:
        s = s[:i]+x
    return s