# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''
    Esta função recebe uma string, um caractere, um número (correspondido entre 0 e o comprimento da string)
    e retorna uma outra string com o caractere informado substituido na posição correspondente ao número informado.
    
    Parametros
    ----------
    s (string) : string
    x (string) : caractere
    i (int) : número
    '''
    s1 = s[:i]
    s2 = s[i+1:]
    return s1+x+s2