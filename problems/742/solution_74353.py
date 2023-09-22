def substitui(s,x,i):
    if len(s[i] in s)==1:
        return s.replace(s[i],x)
    else:
        s2=s.replace(s[i],x)
        return s2.replace(s2[i],s[i],1)