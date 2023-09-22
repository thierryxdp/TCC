def substitui(s,x,i):
    '''Recebe uma string s, um caractere x e um número
    inteiro i entre 0 e o comprimento da string, e
    retorna uma string igual a s, com o elemento de
    posição i substituído pelo caractere x
    string, int, int -> string'''
    metade1 = s[0:i]
    metade2 = s[i+1:]
    return metade1 + x + metade2