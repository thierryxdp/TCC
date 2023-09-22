def substitui(s,x,i):
    '''
    substitui o elemento de posição i da string s
    pelo caractere x
    
    string, string, int -> string
    '''
    parte1 = s[0:i]
    parte2 = s[0:i+1]
    S = parte1+x+parte2