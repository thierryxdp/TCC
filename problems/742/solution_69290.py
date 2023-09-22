def substitui(s,x,i):
    '''Recebe uma string, um caractere x e um número 
    inteiro entre 0 e o comprimento da string.
    string,string,int -> string,int'''
    return s.replace(s[i][0],x)