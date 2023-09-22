# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''função que substitui o elemento de posição i pelo caractere x na string;string,int,int-->string'''
    z=i+1
    return s[:i]+x+s[z:]