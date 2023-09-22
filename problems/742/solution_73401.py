# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    n = list(s)
    l = n.index(n[i])
    if l==i:
        n[i] = x
        strn = ''.join(n)
        return strn
    else:
        return s