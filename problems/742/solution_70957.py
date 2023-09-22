# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Função que substitui um elemento de uma string s por um elemento x na posição i
    str, int, int -> str'''
    return s[0:i]+x+s[i+1:]