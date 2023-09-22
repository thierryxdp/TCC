# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    substitui= "s"+"x"+"i"
    x1=s[0:]
    x2=x
    x3=str(i)[3:0]
    s.replace(x2,x3)
    return x1+x2