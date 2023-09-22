# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Funcao que recebe uma string, um caracter e um numero inteiro (entre 0
e o comprimento da string), retornando uma string igual a s, exceto que o
elemento da posicao i deve ser substituido pelo caracter x"""
    return s[:i] + x + s[i+1:]