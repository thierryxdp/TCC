def substitui(s,x,i):
    '''funcao'''
    s1 = s
    s2 = s1[0:i] +str(x)+s1[i+1:]
    return s2