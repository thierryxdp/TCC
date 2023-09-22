# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    a=list(s)
    a[i+1]=x
    a.replace(',','')
    return(a)