def substitui(,x,i):
    '''calcula string que substituia o caractere de posição i por x
    str,int,int->str'''
    
    str(s)[i] = x
    
    return s[0:i] + x + s[(i+1):]