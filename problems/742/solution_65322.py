def substitui(s,x,i):
    '''Funcao recebe uma string s, um caractere x e um número inteiro i entre 0 e o comprimento da string
string, int -> string'''
    string1 = s[0:i]
    string2 = s[i+:]
    return string1 + str(x) + string2