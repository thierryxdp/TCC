def uppCons(frase):
    r = []
    for e in frase:
        if e not in ("a","e","i","o","u","ã","é","ó"):
                 r.append(e.upper())
    	else:
                 r.append(e)
    return str.join("",r)