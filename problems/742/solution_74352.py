def substitui(s,x,i):
    s2=s.replace(s[i],x)
    return s2.replace(s2[i],s[i],1)