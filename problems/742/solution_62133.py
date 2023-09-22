# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Recebe uma string s, um caractere x e um número inteiro i cujo valor está entre zero e o comprimento da string,
    e retorna uma string igual a s, esceto que o elemento da posição i deve ser subtituido pelo caractere x.
    str, str, int ---> str'''
    
    return s[:i] + str(x) + s[(i-1):]