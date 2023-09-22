# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Esta funcao substitui um caractere de uma string na posicao indicada por um numero inteiro.'''
    antes_de_x = s[:i]
    depois_de_x = s[i + 1:]
    return antes_de_x + x + depois_de_x