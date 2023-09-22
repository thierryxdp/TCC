def substitui (s, x, i):
    '''Função que recebe uma string s, um caractere x e um número inteiro i
entre 0 e o comprimento da string, e retorna uma string igual a s, exceto que o
elemento da posição i é substituído pelo caractere x.'''
    #string, string, int -> string
    #funciona com números
    s = str(s)
    x = str(x)
    return s[0:i] + x + s[i + 1:]