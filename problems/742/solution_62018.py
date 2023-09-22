# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    sub_s1 = s[0,i]
    sub_s2 = s[i]
    return sub_s1 + x + sub_s2