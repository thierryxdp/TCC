# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Função que recebe uma string s, um caractere x e um numero inteiro i que deve estar entre 0 e o comprimento da string s, e retorna uma string com o caractere x dado pela posição i.'''
    '''string, string, int -> string'''
    return s[ : i] + x + s[i + 1 : ]