# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Função que recebe uma string s, um caractere x e um numero i entre 0 e o comprimento da string e retorna uma string onde o elemento da posição i é substituido pelo caractere x.'''
    '''string, int, int -> string'''
    return s[ : i] + x + s[i + 1 : ]