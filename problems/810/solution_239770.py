def inverte(frase): 
	frase=frase.replace("."," ")
    frase=frase.replace(","," ")
    frase=frase.replace("-"," ")
    frase=frase.replace(":"," ")
    frase=frase.replace(";"," ")
    frase=frase.replace("!"," ")
    frase=frase.replace("?"," ")
    frase1=str.split(frase," ")
    frase2=frase1[::-1]
    frase3=str.join(" ",frase2)
    return frase3.lower()