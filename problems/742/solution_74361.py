def substitui(s,x,i):
    if s.count(s[i])==1:
        return s.replace(s[i],x)
    if s.find(s[i]) == i or s.find(x)>=0:
        return s.replace(s[i],x,1)
    else:
        s2=s.replace(s[i],x)
        return s2.replace(s2[i],s[i],1)