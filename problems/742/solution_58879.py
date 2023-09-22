def substitui(s,x,i):
    t= len(s)
    r= s[0:i]+str(x)+s[(i+1):t]
    return r