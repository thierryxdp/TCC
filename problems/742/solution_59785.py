# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Funcao retorna uma string igual a s, exceto o elemento da posicao i, que sera substituido por x'''
    return s[0:i] + x + s[i+1: len(s)]