# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Essa função, faz com que o valor informado de i
    indique qual letra será trocada, e o valor x,
    será a letra substituta"""
    l=list(s)
    l[i]=x
    s="".join(l)
    return s