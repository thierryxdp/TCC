# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(str,x,i):
    str[i] = x
    return str[0:i] + x + str[i + 1:]