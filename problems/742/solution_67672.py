# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    limite = s[0:i]
    subs = s.replace(limite, x, 1)
    return subs