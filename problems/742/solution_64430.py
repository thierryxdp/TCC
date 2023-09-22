# Coloque um comentário dizendo o que a função faz
# string, int, int -> string
def substitui(str1, x, i):
    str1[i] = x
    return str1[0:i] + x + str1[i+1:]