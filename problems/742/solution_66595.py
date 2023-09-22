# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """funão que recebe uma str, int e um caractere e faz uma substituição
str,int>str"""
    return s[i:] + str(x) + s[1+i:]