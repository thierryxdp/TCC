def substitui(s,x,i):
    '''Retorna a string s com uma substituição na posição i pelo caracter x.
    str, str, int -> str'''
    return str(s)[0:i] + str(x) + str(s)[(i+1):len(s)]