# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
import bytearray

def substitui(s,x,i):
	l = bytearray(s)
    l[i]=x
    return l[i]