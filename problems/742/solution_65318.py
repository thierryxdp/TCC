def substitui(s,x,i):
    '''Funcao recebe uma string s, um caractere x e um número inteiro i entre 0 e o comprimento da string
string, int -> string'''
    string = s[:i]
    return string + str(x)