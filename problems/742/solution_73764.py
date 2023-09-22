def substitui(s,x,i):
    '''
    funcao que recebe uma string s, um caractere x e um numero
    inteiro i entre 0 e o comprimento da string, e retorna uma 
    string igual a s
    :param s: str
    :param x: int
    :param i: int
    :return: str
    '''
    return s[0:i]+ x +s[i+1:]