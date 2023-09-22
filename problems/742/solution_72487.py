def substitui(s,x,i):
    '''função que recebe uma string s, um caractere x e um número inteiro i entre 0 e o comprimento da string, e retorna
    string, int, int -> string'''
    return s[0:i]+x+s[i+1:len(s)]