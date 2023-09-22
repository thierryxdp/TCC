def inverte(frase): 
	frase=frase.replace("."," ")
    frase=frase.replace(",","")
    frase=frase.replace("-"," ")
    frase=frase.replace(":"," ")
    frase=frase.replace(";"," ")
    frase=frase.replace("!"," ")
    frase=frase.replace("?"," ")
    frase1=str.split(frase," ")
    frase2=frase1[::-1]
    frase3=str.join(" ",frase2)
    frase4=frase3.split(' ', 1)[1]
    return frase4.lower()