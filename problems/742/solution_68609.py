# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    s=list(s)
    s[i]=x
    return s[0:] + x + s[i + 1:]