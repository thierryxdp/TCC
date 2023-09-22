# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    antes = s[0:i]
    dps = s[i+1:]
    return antes+x+dps