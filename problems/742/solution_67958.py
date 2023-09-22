# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ls= i-len(s)
    li= i-len(s)+1
    Str= s[:ls]+str(x)+s[li:]
    return Str