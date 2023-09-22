# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """substitui um caractere por fatiamento. string, int, int -> string"""
    return s[0:i] + x + s[len(i+1):len(s)]