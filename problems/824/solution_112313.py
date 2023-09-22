def uppCons(s):
    l=list(s)
    x=0
    r=""
    vogais=["a","e","i","o","u","ã","õ","ô","é","ó","ú"]
    while x<len(l):
        if l[x] not in vogais:
            l[x]=l[x].upper()
		x+=1
    
	for k in l:
        r+=k
	return r