def substitui(s,x,i):
    '''calcula uma string igual a s com substituicao  de i pelo x'''
    if i==0:
        return x+s[1:]
    elif i==len(s):
        return s[0:len(s)]+x
    elif i>0 and i<len(s):
        return s[0:i]+x+s[i+1:]