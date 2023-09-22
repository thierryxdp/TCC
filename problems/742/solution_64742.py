# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(strs,x,i):
    strs [i] = x
    return strs[0:i] + x + strs[i + 1:]