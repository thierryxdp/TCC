def substitui(s,x,i):
    '''str,int,int -> str'''
    string=s
    return str.strip(string[:i]+str(x))+string