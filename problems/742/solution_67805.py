# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    l=len(s)
    if 0<=i<=l:
        r=list(s)
        r[i]=str(x)
        s="".join(r)
        return s
    if i>l:
        return " "