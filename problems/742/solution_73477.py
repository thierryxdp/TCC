# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    "Substitui um termo x em uma str s na posiçao i.str,int,int->str"
    return s[:i]+str(x)+s[i+1:]