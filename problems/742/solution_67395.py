# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    substitui= "s"+"x"+"i"
    x1=s[0:1]
    x2=str(i)[3:]
    x3=x
    s.replace(x1,x2)
    return x1+x2+x3