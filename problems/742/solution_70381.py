# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''str,int,int -> str'''
    return s[:i]+str(x)+str.index(s,x)