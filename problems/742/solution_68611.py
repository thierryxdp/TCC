# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''substitui o caracter i pelo caracter x em uma determinada string.'''
    0 >= i <= len(s)
    return s[:i] + str(x) + s[i+1:]