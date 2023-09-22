# Substituição.
def substitui(s,x,i):
    '''Esta recebe uma frase, um caractere e um número inteiro entre 0 e o tamanho da frase e retorna 
    a frase substituindo o elemento da frase pelo elemento de entrada
    na posição inserida com o inteiro;
    STR, STR/FLOAT, INT -> STR'''
    s[i]=x
    return s