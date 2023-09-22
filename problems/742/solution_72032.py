def substitui(s,x,i):
    '''Recebe uma string s retorna a string, mas com o elemento da posição substituído pelo item x
    '''
    return str(s[:i])+x+str(s[i+1:])