def substitui(s,x,i):
    '''Substitui a letra colocada em 'x' na palavra colocada em 's' de acordo com o numero colocado em 'i' '''
    nova = s.replace(s[i], x)
    return nova