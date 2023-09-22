# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''função que, dados uma string (s), um caractere (x) e um número inteiro
    (i) entre 0 e o comprimento da string, retorna uma string igual a (s), mas
    com o elemento da posição (i) substituído pelo caractere (x);
    str, caractere, int -> str'''
    return s[:i] + x + s[(i+1):]