def uppCons(frase):
    
    x = list(frase)
    y=[]
    for letra in x:
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" or letra == "í" or letra == "ã" or letra == "ó" or letra == "ú" or letra == "é":
        	y.append(letra)
        else:
            w=letra.upper()
			y.append(w)
    return "".join(y)