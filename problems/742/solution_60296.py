# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''função que dado S,X,I, retorna uma string igual a s, porém com o elemento da posição i substituiído pelo x. string, int, int, -> string'''
    return s[0:i]+x+s[i+1:]