# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    s1= list(s)
    s1[i]=x
    s2=''.join(s1)
    return s2