def substitui(s,x,i):
    if i==0:
        
        b=s[i+1:]
        return x + b
    else:
        a= s[:i]
        i=x
        return a+i+ b