# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    comprimento = len(s)
    if 0<=i<=comprimento:
        s[i] = x
        return