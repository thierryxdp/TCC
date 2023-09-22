def lingua_p(palavra):
    vogais=["a","e","i","o","u","é","á","ú","ó","ô","ê","ã","õ"]
    l=list(palavra)
    r=[]
    s=""
    for x in l:
        if x.lower() in vogais:
            r.append(x+"p"+x)
		else:
            r.append(x)
	for y in r:
        s+=y
	return s