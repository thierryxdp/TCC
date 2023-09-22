# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Substitui uma determinada letra em uma string
       string int int --> string'''
    nova_palavra = s[:i] + x + s[i+1:]
    return nova_palavra