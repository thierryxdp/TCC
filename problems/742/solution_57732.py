# Substituição.
# string, int, int -> string
def substitui(s,x,i):
    '''Essa função recebe uma frase, um caractere e um número inteiro, e retorna a frase com o caractere inserido na posição  dada pelo inteiro inserido;
    STR, INT, INT -> STR'''
    return s[0:i]+x+s[i+1:]