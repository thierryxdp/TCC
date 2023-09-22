def substitui(s,x,i):
    s = str(s)
    return s[0:x-1] + i + s[x+1:len(s)]