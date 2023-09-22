# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''substitui um elemento da string por outro'''
    '''str,str,int -> str'''
    return s[0:i] + x + s[i+1:]