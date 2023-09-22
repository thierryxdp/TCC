# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Substitui um caracter da string por outro'''
    string=s[0:i]+x+s[i+1:]
    return string