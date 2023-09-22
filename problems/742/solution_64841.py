# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    y=s
    if i>=0 and i<=len(s):
        return y[0:i]+x+y[(i+1):-1]