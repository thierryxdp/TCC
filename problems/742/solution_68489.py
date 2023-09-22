# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    letra = x
    palavra = s[0:i] + letra + s[i+1:]
    return palavra