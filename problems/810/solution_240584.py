"""Retorna a frase invertida:
str->str"""
def inverte(frase):
    frase.reverse()
	if '.':
    	frase = str.split(frase, ".")
    	frase = str.join(" ", frase)
    if ',':
        frase = str.split(frase, ",")
    	frase = str.join(" ", frase)
    if '...':
        frase = str.split(frase, "...")
    	frase = str.join(" ", frase)
    if '?':
        frase = str.split(frase, "?")
    	frase = str.join(" ", frase)
    if '-':
        frase = str.split(frase, "-")
    	frase = str.join(" ", frase)
    if ':':
        frase = str.split(frase, ":")
    	frase = str.join(" ", frase)
    if '!':
        frase = str.split(frase, "!")
    	frase = str.join(" ", frase)
    return frase