# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    posi = i - 1
    nova = s[:posi]+x+s[i:]
    return nova