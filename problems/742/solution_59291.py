# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    x = x[-1] + x[1:-1] + x[0] if len(s) > 1 else x
    substitui = s.replace(s[i],x,)
    return substitui