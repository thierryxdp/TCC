# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''susbtitui um carcter na posição i de uma string s pelo carcter x
    entradas: (string,carcter,posicao_do_carcter)
    str, str, int -> str'''
    if 0 <= i < len(s):
        return s[:i] + x + s[(i+1):]