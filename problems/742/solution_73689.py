# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ""
    lim = len(s)
    
    if lim >= i:
        i = x
        m = s[i]
    return m