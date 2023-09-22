def substitui(s,x,i):
    if i>0 and i<len(s):
        return s[:i]+x+s[i+1:]