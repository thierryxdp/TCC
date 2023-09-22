# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''função que substitui um caractere de uma string (s)
    por um caractere (x) na posição indicada pelo elemento
    na posiçao (i) que é um numero inteiro'''
    return s[0:i] + x + s[i+1:]