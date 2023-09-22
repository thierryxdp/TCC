def substitui(s,x,i):
    '''Recebe uma string, um caractere e um inteiro, e retorna uma string com o caractere da posição i alterado pelo
    caractere x
    string, caractere, int -> string
    '''

    s = s[:i] + x + s[i+1:]
    
    return s