# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
       t=s[0:i]
       t=t+str(x)
       return t+t[i:]