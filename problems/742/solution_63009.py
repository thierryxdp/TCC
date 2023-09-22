# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    LS = i-len(s)
    LI = i-len(s)+1
    Str = s[:LS]+str(x)+s[LI:]
    return Str