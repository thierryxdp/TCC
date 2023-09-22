# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''substitui um caractere da string s por um outro x em uma certa posição i'''
    return s[0:i-1] + x + s[i:]