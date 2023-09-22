def substitui(s,x,i):
    if i==0:
        return x + s[1:len(s)+1]
    else:
        return s[0:i] + x + s[i+1:len(s)+1]