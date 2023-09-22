def uppCons(frase):
    
    x = list(frase)
    y=[]
    for letra in x:
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" or letra == " " or letra == "," or letra == "!" or letra == "?":
        	y.append(letra)
        else:
            w=letra.upper()
			y.append(w)
    return " ".join(y)