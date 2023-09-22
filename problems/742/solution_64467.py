# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''substitui o elemento da posição i da string s pelo caractere x
    str,int,int -> str'''
    comp = len(s)
    if i>=0 and i<=comp:
        s[i] = x
    return s