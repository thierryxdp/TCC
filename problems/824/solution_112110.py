def i(b):
    vogais=["a","e","i","o","u","A","E","I","O","U","ã","á","é","í","ó","ú"]
    return str.upper(b) if b not in vogais else b
def uppCons(frase):
	fraseA=str.join("",map(i,frase))
	return fraseA