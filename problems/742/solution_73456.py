def substitui(s,x,i):
    '''Esta função mescla conceitos de strings e fatiamento'''
    s = s[0:i] + x + s[i + 1:]
    return s