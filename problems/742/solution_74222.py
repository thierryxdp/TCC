# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    aux = s[0:1] + x + s[i+1:len(s)]
    return aux