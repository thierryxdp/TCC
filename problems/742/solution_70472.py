# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ''' Substitui o carcter i pelo carcter x'''
    0 >= i <= len(s)
    return s [0:i] + x + s [i + 1:]