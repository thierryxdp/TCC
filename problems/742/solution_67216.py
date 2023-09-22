def substitui(s,x,i):
    
    '''Funcao que recebe os parametros (s, x, i)
    e retorna uma string (s) onde o elemento de uma
    dada posicao (i) foi substituido por (x).
    
    :param (s, x, i): str
    :return: str
    '''
    
    return s[:i] + 'x' + s[i:]