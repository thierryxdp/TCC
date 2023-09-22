def uppCons(frase):
    a=len(frase)
    b=0
    while b<a:
        if frase[a]!="a","e","i","o","u","A","E","I","O","U":
            frase[a]=str.upper(frase[a])
            b=b+1
	return frase