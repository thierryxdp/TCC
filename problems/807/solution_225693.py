def conta_frase(frase):
   	frase1 = frase.split(".")
    frase2 = frase.split("?")
    frase3 = frase.split("!")
    frase4 = frase.split("...")
	frase5 = frase.split(";")
    n = (len(frase1)+len(frase2)+len(frase3)+len(frase4))
    return n