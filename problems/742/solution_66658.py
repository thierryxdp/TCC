# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    if 0>i:
        return str(s[x+i])
    elif 0<=i:
        return str(s)