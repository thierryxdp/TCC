# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''
    funcao que recebe uma string s, um caractere x e um numero
    inteiro i entre 0 e o comprimento da string, e retorna uma 
    string igual a s
    :param s: str
    :param x: int
    :param i: int
    :return: str
    '''
    return s[:1]+x+s[i+0:]