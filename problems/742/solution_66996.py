# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''retorna string = s, exceto pelo elemento que se encontra
    na posiçãi I, que será substituido pelo X.'''
    s[i]=x
    return s[0:i] + x + s[i+1:]