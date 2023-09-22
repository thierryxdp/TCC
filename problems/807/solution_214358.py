def conta_frases(texto):
    contador1 = str.count(texto,"...")
    contador2 = str.count(texto,"?")
    contador3 = str.count(texto,"!")
    if contador1>0:
        return contador1+contador2+contador3
    else:
    contador4 = str.count(texto,".")
    	return contador1+contador2+contador3+contador4