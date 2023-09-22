def uppCons(frase):
    r=""
	for x in frase:
        if x in ["a","e","i","o","u"]:
            return r+=x
        else:
            return r+=(x.upper)
	return r
    
    
















def uppCons(frase):
    r=[]
    for x in frase:
        if x in ["a","e","i","o","u"]:
            return x