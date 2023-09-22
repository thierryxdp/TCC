# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    str1 = s
    str2 = str1[0: i] + x + str1[i+1 :]
    return str2