# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''substitui um caractér da string (s) por um caratér (x)
    na posição (i) da string
    str, str, int -> str'''
    return s[0:i]+str(x)+s[i+1:]