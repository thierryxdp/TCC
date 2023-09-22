def substitui(s,x,i):
    '''função que recebe string, caractere, número e comprimento da string
    retorna uma string s'''
    'str,str,int->str'
    return s[:i] + x + s[i+1:]