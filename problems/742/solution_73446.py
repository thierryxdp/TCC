def substitui(s,x,i):
    '''Esta função mescla conceitos de strings e fatiamento'''
    s[i] = x
    return s[0:i] + x + s[i + 1:]