def substitui(s,x,i):
    '''função que recebe string, caractere, número e comprimenro da string e retorna uma string s'''
    'str,str,int->str'
    return s[:i] + x + s[i+1:]