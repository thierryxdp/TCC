# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    11 >= i >= 0
    if i == 0:
        s = str(x) + s[1:11]
        return s[0:11:1]
    elif i == 1:
        s = s[0:1] + str(x) + s[2:11]
        return s[0:11:1]