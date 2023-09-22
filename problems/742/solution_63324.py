def substitui(s,x,i):
    ''' Retorna string iual a s, exceto que o elemento da
        posição i deve ser substituído pelo caractere x
        str, caractere, int -> str
    '''
    return s[0:i] +str(x)+s[i+1:]