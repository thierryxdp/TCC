def conta_frases(texto):
    x=str.count(texto,"!")
    x=x+str.count(texto,"?")
    x=x+str.count(texto,"...")
    if "..." in texto:
   		x=x+str.count(texto,".")-(str.count(texto,"..."))*3
	else:
        x=x+str.count(texto,".")
    return  x