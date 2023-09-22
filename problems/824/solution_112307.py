def uppCons(s):
    l=list(s)
    r=""
    vogais=["a","e","i","o","u"]
    while x<len(l):
        if l[x] not in vogais:
            l[x]=l[x].upper
	x+=1
    
    for x in l:
        r+=x
	return r