# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''substitui o elemento da posição i da string s pelo caractere x
    str,int,int -> str'''
    return s[0:i]+x+s[-1:i:-1]