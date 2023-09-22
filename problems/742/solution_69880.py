# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''substitui o elemento da posição i da string s pelo caractere x;
    str, str, int -> str'''
    s[i] = x
    return s