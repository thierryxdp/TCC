# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    s[i] = str(x)
    t = s[0:i] + str(x) + s[i + 1:]
    return t