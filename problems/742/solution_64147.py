# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    aux = ''
    for k in range len(s):
        if k == i:
            aux += x
        else:
            aux += s[k]
    return aux