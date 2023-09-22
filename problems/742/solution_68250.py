# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Função que recebe uma string s, um caractere x e um 
    número i, retornando uma string igual a s com o elemento
    da posição i senso substituído pelo caractere x.
    0<i<len(s)
    str, str, int -> str'''
    return s[0:i] + x + s[i+1:]