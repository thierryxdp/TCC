def substitui(s,x,i):
	if i==0:
    	return s[i]+s.replace(s[i:],x)
    if i>0:
    	t=i+1
        return s[0:i]+s.replace(s[:t],x)