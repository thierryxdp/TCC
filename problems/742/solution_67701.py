# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    p1=s[i+1:]
    p2=s[:i]
    return p2+x+p1