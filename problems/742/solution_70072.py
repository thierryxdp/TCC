# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Substitui um caractere(x) de uma string(s)
    	de acordo com a posição i escolhida.
        str,int,int -> str'''
    l = list(s)
    l[i] = x
    s = ''.join(l)
    return s