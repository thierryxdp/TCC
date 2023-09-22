# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    t=(s[:i])
    y=t+str(x)
    a=(s[i+1: ])
    return str(y)+str(a)