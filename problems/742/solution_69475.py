# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Retorna uma string s de com uma caractere x na posição i
    string, int, int -> string'''
    l = [s, x, i]
    l[i] = str(x)
    return l