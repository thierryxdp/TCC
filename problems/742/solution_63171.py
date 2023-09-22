# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    sl=list(s)
    sl[i]= x
    s="".join(sl)
    return s