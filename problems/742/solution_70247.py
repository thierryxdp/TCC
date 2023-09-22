# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''substitui o elemento da posição i em uma string s
    por um caractere x
    str, str, int -> str'''
    return s[0:i]+x+s[i+1:len(s)]