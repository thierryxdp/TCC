# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    i1=i+1
    substituida=s[:i]+s[i1:]
    adicionar=x
    substituida2=substituida[i:]+adicionar
    return substituida2