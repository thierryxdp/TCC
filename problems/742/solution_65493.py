# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''retornar a string de entrada s, substituindo o elemento da posição i de entrada pelo caractere x de entrada'''
    return s[0:i]+x+s[i+1:]