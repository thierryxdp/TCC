def uppCons(frase):
    r=""
	for x in frase:
        if x in ["a","e","i","o","u"]:
            return r.append(x)
        else:
            return r.append(x.upper)
	return r
    
    
















def uppCons(frase):
    r=[]
    for x in frase:
        if x in ["a","e","i","o","u"]:
            return x