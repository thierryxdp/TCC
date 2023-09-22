def substitui(s,x,i):
	if i>0:
    	t=i+1
        return s[0:i]+s.replace(s[:t],x)
	else i=0:
    	return s[0:i]+s.replace(s[:0],x)