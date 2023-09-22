# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    pt1 = s[:i]
    pt2 = s[i+1:]
    return pt1 + x + pt2