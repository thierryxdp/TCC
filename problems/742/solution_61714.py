# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    a=len(s)
    corte=s[0:i]
    sobra=[i:len(s)]
    return corte+x+sobra