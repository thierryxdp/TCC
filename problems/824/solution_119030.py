def uppCons(frase):
    r = []
    for e in frase:
        if e not in ("a",'e","i","o","u"):
                 r.append(e.upper())
    	else:
                 r.ppend(e)
    return str.join("",r)