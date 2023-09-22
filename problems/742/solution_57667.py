# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''dada uma string s, substitui o caracter orginal na posicao i pelo caracter x
    str, str, int -> str'''
    return s[:i] + x + s[i+1:]