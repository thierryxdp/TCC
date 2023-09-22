# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ant=s[0:i:1]
    dps=s[i:-1:1]
    sub=ant+x+dps
    return dps