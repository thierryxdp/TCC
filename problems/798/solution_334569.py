def freq_palavras(frases):
    fDividida=frases.split()
    resultado={}
for palavra in fDividida:
    if palavra in resultado:
		resultado+=1
    else:
        resultado=1
return resultado