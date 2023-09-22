"""Retorna a frase invertida:
str->str"""
def inverte(frase):
    if '.':
    	frase = str.split(frase, ".")
        lista.reverse()
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