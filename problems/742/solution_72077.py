def substitui(s,x,i):
    '''
    s = () "string
    x = i
    i = len (s)
    string, int, int --> string '''
    string0=str(s)
    string1=string0[0:i]
    string2=string0[i+1:]
    return str(string1)+str(x)+str(string2)