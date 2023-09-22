def substitui(s,x,i):
    '''uma str s, um caractere x
    e um numero inteiro  i entre 0 e o comprimento da str
    retornando s com o caracter da posição i trocado por x
    string, int, int -> string'''
    return s[0:(i+1)]+x+s[i+2:]