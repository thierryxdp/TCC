# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    contar = len(s)
    subs = x.replace(s[i], x)
    return subs