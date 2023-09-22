def substitui(s,x,i):
    #0<i<len(s)
    #str,str,int -> str
    return s[0:i] + x + s[i+1:]