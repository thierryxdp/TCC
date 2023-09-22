def inverte(frase):
    """ Função que, dado uma frase, retorne a mesma frase inversa.
    str->str"""
    f1=frase.replace("-", " ")
    f2=f1.replace(",", " ")
    f3=f2.replace(":", " ")
    f4=f3.replace("!", " ")
    f5=f4.replace("?", " ")
    f6=f5.replace(".", " ")
    
	if f6:
		return f6.split(" ")
	if f6:
		return f6.join(" ")
    if f6:
		return f6.join(" ")
    if f6:
		return f6.lower
    return f6[::-1]