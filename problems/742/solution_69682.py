def substitui(s,x,i):
    '''Funcão que retorne uma string, exceto que o elemento da posicão i deve ser substituido pelo x'''
    return s[:i] + str(x) + s[i+1:]