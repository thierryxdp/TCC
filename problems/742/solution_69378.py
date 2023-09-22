# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    0<i<=len(s)
    i2= i + 'x'
    s = s[:i] + x + s[i2:]
    return s