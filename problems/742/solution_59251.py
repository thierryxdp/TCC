# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,w):
    s = s+''
    x = x+''
    z = s[w]
    substitui = s.replace(z,x)
    return substitui