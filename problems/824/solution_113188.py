def uppCons(frase):
	
    str.upper(frase)
    while 'AEIOU' in frase:
        str.replace(frase,'AEIOU','aeiou')
    return frase