# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Substitui, na string s, o caractere na posição i pela letra informada em x.
    str,str,int-> str'''
    return s[0:i]+x+s[i+1:]