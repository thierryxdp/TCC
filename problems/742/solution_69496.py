# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Retorna uma string s de com uma caractere x na posição i
    string, int, int -> string'''
    new_s = s[:i] + str(x) + s[i:]
    return new_s