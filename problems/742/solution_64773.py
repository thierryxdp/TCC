# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    if i == 0:
        return x + (s[1:])
    if i == len(s):
        q = len(s)-1
        return (s[0:q]) + x
    if len(s) < i < len(s):
        (s[0::i]) + x + (s[i+1:])