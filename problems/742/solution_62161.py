# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    meio = s[0:i]
    meio2 = s[i:-1]
    return str(meio + x + meio2)