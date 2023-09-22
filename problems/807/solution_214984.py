def conta_frases(s):
    x= str.split(s,".",)
    y= str.split(s,"!",)
    z= str.split(s,"?",)
    w= str.split(s,"...",)
	return len(x)+len(y)+len(z)+len(w)