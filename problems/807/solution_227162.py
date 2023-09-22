def conta_frases(frases):
	    frase=0
	    if '...' in frases:
	     frase+=(len(str.split(frases,'...')))-4
	    if '.' in frases:
	     frase+=(len(str.split(frases,'.')))-(1*(len(str('....'))))
	    if '!' in frases:
	     frase+=(len(str.split(frases,'!')))-1
	    if '?' in frases:
	     frase+=(len(str.split(frases,'?')))-1
	     return frase
	     
	    else:
	        return True