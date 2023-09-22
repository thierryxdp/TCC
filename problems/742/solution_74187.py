def substitui(s,x,i):
    '''Recebe uma string, um caractere e um inteiro, e retorna uma string com o caractere da posição i alterado pelo
    caractere x
    string, int, int -> string
    '''

    s = s[:i-1] + x + s[i:]
    
    return s