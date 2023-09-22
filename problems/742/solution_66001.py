# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """A função ao receber uma string "s", um caractere "x" e um número
    "i" inteiro entre 0 e o comprimento da string retorna uma string
    igual a "s", mas o elemento da posição "i" é substituído pelo
    caractere "x".
    str, int, int -> str"""
    
    return str(s)[0:i] + str(x) + str(s)[i+1:]