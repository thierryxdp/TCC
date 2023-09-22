def substitui(s,x,i):
    '''str,int,int -> str'''
    string=s
    return string[:i]+str(x)+str.strip(string[:])