# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Função que substitui um caracter de uma strinh por outro, dê como parametro da funcao a string, o caracter e a posição a ser modificada, respectivamente.'''
    pt1= s[0:i]
    pt2= s[1+i:]
    return pt1+str(x)+pt2