"""Retorna a frase invertida:
str->str"""
def inverte(frase):
    if '.':
    	frase = str.split(frase, ".")
        frase.reverse()
    	frase = str.join(" ", frase)
    if ',':
        frase = str.split(frase, ",")
        frase.reverse()
    	frase = str.join(" ", frase)
    if '...':
        frase = str.split(frase, "...")
        frase.reverse()
    	frase = str.join(" ", frase)
    if '?':
        frase = str.split(frase, "?")
        frase.reverse()
    	frase = str.join(" ", frase)
    if '-':
        frase = str.split(frase, "-")
        frase.reverse()
    	frase = str.join(" ", frase)
    if ':':
        frase = str.split(frase, ":")
        #frase= list.reverse(frase)
		frase.reverse()
    	frase = str.join(" ", frase)
        
    if '!':
        frase = str.split(frase, "!")
        frase.reverse()
    	frase = str.join(" ", frase)
    return frase