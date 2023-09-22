# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """"""
    nc = len(s) - i
    nc2 = str.find(nc)
    return str.replace(s, str(x), nc2)