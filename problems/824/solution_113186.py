def uppCons(frase):
	
    str.upper(frase)
    while 'A' in frase:
        	str.replace(frase,'A','a')
    while 'E' in frase:
        	str.replace(frase,'E','e')
  	while 'I' in frase:
            str.replace(frase,'I','i')
    while 'O' in frase:
            str.replace(frase,'O','o')
    while 'U' in frase:
            str.replace(frase,'U','u')
            
    return frase