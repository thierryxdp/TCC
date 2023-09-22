def uppCons(s):
    l=list(s)
    x=0
    r=""
    vogais=["a","e","i","o","u"]
    while x<len(l):
        if l[x] not in vogais:
            l[x]=l[x].upper
		x+=1
    
	for k in l:
        r+=l
	return r