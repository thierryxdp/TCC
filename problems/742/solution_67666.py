# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    limite = s[i:]
    subs = s.replace(limite[0], x)
    return subs