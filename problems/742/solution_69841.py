def substitui(s,x,i):
    '''
    '''
    
    if i == 0:
        return x+s[1:]
    elif i == [len(s)]:
        return s[len(s)] + x
    elif i == i>0:
        return s[0:i] + x +s[i+1:]