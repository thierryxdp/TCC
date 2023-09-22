def substitui(s,x,i):
    '''substitui letra na posição escolhida'''
    '''str-->str'''
    p1 = s[0:i]
    p2 = s[i+1:len(s)]
    return p1 + x +p2