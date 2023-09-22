# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """ funcao que substitui o elemento de posicao i, por x na string s"""
    s = s[:i] + x
    return s