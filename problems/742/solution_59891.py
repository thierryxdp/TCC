def substitui(s,x,i):
    tamanho=len(s)
    i=i
    x=str(x)
    if 0<=i<=tamanho:
        return s[0:i]+x+s[((i+1):]