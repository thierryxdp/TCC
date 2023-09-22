def posLetra(frase,letra,oco):
    i=0
    pos=0
    ocototal = str.count(frase,letra)
    if oco<ocototal:
        while i<len(frase):
            if frase[i]==letra:
                pos+=1
                if pos == oco:
                    return i
            i+=1
	else:
        return -1