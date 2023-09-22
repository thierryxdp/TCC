def uppCons(frase):
	
    str.upper(frase)
    while 'AEIOU' in frase:
        str.lower(frase,'AEIOU','aeiou')
    return frase