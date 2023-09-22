def substitui(s,x,i):
    h = s[0:i]
    p = s[i+1::] 
    if p == "" :
        return h + x + p 
    else:
    	return h + x + p