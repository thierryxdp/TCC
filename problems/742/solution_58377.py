def substitui(s,x,i):
    ''' esta funcao retorna uma string igual a s mas substitui o elemento da posicao i pelo caractere x'''
    s = list(s)
    s[i] = x
    return ''.join(s)