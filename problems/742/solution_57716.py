# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Pede uma string, um caractere e um inteiro entre zero
    e o comprimento da string e retorna a mesma string,
    substituindo o caractere x pelo que estiver na posição i
    da string original.
    str, int, int ->string"""
    nova_string=s[:i]+x+s[(i+1):]
    return nova_string