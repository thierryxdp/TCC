def substitui(s,x,i):
    '''Recebe uma string s, um caracter x e um inteiro i e 
    substitui o caracter correpondente à posição i pelo caracter x
    string, caracter, int -> string'''
    
    s.replace(s[i],x)
    return s