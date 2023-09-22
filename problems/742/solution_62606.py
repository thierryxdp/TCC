# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    if int i<0:
    return s+x
    if i>len(s):
    return s+x
    else:
        return s[:1]+x+s[i+1:]