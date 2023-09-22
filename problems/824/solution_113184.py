def uppCons(frase):
	
    str.upper(frase)
    while 'A' in frase:
        	str.replace(frase,'A','a')
    while 'B' in frase:
        	str.replace(frase,'E','e')
  	while 'B' in frase:
            str.replace(frase,'I','i')
    while 'B' in frase:
            str.replace(frase,'O','o')
    while 'B' in frase:
            str.replace(frase,'U','u')
            
    return frase