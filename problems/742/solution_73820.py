# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    x1=x+1
    substituida=s[:x]+s[x1:]
    substituida2=[i]+substituida[x:]
    return substituida2