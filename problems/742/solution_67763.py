# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''recebe uma string um caractere x e um numero inteiro,
    e retorna a string com o caractere x na posição do numero inteiro
    str, int, int -> str'''
    return s[0:i]+x+s[i+1:]