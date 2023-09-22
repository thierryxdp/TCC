lingua_p(frase:str)->str:
i=0
    while x<len(frase):
    	if frase[x] in "aeiou":
    		frase=frase[0:x+1]+"p"+[x+2:]
        i=i+1
   	return frase