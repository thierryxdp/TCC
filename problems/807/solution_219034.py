def conta_frases(texto):
    contador = 0
    for i in range (0,len(texto)):
        if texto [i] == ".":
			if texto [i-1] == ".":
            	if texto [i-2] == ".":
                	contador +=1
			elif texto [i]!= len(texto)-2:
				if texto[i+1]!=".":
                	contador +=1
		if texto [i] == "!":
            contador +=1
        if texto [i] == "?":
            contador +=1
	return contador