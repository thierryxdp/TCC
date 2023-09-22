def substitui(s,x,i):
    '''
    '''
    if i> len(s):
        return 'inválido'
    else:
    return s[0:i] + str(x) + s[i +1:]