def substitui(s,x,i):
    '''função que recebe string, caractere, numero e comprimento da string return uma string s'''
    'str,str,int -> str'
    return s[:i] + x + s[i+1:]