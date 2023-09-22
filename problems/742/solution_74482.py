def substitui(s,x,i):
    '''Função que recebe string, caractere, número e comprimento da string e retorna uma string s'''
    'str, str, int -> str'
    return s[:i] + x + s[i+1:]