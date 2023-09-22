# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Função que recebe uma string, um caractere e um número
    inteiro que esteja entre 0 e o comprimento da string, e que 
    retorna uma string igual a inicial, porém com o elemento da 
    posição do número inserido substituido pelo caractere posto
    str, str, int -> str'''
    return s[0:i] + str(x) + s[i+1:]