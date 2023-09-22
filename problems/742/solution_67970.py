def substitui(s,x,i):
    '''Retorna uma string igual a s, mas o elemento da posição i
    é substituído pelo caractere x.'''
    return s[0:i] + x + s[i+1:]