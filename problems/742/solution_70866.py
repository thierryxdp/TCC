# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    return parte1(s,i) + str(x) + parte2(s,i)
def parte1(s,i):
    return s[0:i]
def parte2(s,i):
    return [i:-1]