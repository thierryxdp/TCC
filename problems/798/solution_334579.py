def freq_palavras(frases):
    fDividida= frases.split()
    resultado={}
  	for p in fDividida:
      	if p in resultado:
			resultado+=1
      	else:
        	resultado=1
  	return resultado