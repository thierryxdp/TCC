# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''retorna string = s, exceto pelo elemento que se encontra
    na posição I, que será substituído pelo X.'''
    return s[0:i] + x + s[i+1:]