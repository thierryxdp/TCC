# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    sub_s1 = s[1:i]
    return s.replace(sub_s1,x,1)