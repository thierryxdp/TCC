def substitui(s,x,i):
    '''dadas uma string (s), substitui o elemento da posiçao i(inteiro entre 0 e o comprimento da string) pelo caractere (x);
    str, str, int --> str'''
    return s[:i]+x+s[(i+1):]