# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s, x, i):
    '''pegar uma string e um novo caractere e substituir esse novo string no caractere indicado
str,str,int -> str'''
    return s[0:i] + x + s[i + 1:]