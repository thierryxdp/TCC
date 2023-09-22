# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''função que substitui um elemento de uma string por um caractere dado na posição escolhida'''
    s = s[0:i] + x + s[i:]
    return s