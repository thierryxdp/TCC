# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
import random
def substitui(s,x,i):
    i=random.randint(0,len(s-1))
    s = s[0:i] + x + s[i+1: ]
    return s