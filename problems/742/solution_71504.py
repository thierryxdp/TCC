def substitui(s,x,i):
    '''calcula string que substituia o caractere de posição i por x
    str,int,int->str'''
    
    str(s) = s
    s[i] = x
    
    return str(s)[0:i] + x + str(s)[(i+1):]