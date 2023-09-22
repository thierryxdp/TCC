# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Função que recebe uma string s, im caracter x e um numero inteiro i (entre 0 e o comprimento da string) e retorna uma string igual porém com o elemento da posição i substituido pelo caracter x.'''
    s[i] = x
    return s