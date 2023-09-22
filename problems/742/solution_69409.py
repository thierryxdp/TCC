def substitui(s,x,i):
    '''Recebe uma string s, um caractere x e um número inteiro i e retorna
    uma string igual a s.
    string,string,int -> string'''
    
    return s[0:i] + x + s[i+1:]