def substitui(s,x,i):
    '''Funcao que recebe uma string, caractere, número que indica um índice da string
    e retorna uma string igual, com alteração no índice informado pelo caractere informado
    str, str, int -> str'''
    return s[:i] + x + s[i+1:]