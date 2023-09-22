# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    l=list(s)
    l[i]=x
    s="".join(l)
    return s
    """new_s=s.replace(s[i],x)
    return new_s"""