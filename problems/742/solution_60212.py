# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    b = str(s)
    x = str(x)
    s[i] = x
    return s[0:i] + x + s[i+1:]