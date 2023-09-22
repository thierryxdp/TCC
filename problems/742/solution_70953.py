def substitui(s,x,i):
    a=s[:i-1]+x+s[i+1:]
    return s.replace(i,a)