# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''str, int, int -> str
    substitui um caractere(i) da string(s) por um
    outro(x)'''
    I=i+1
    return s[:i]+x+s[I:]