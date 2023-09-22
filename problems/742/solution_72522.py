# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Essa função recebe uma palavra e substitui uma letra selecionada por uma letra desejada
    string, int, int -> string'''
    var = str(s)
    return var[:i] + str(x) + var[(i+1):]