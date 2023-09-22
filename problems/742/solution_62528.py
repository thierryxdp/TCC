# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    s1 = s[:i]
    s2 = s[i+1:]
    return s1 + x + s2