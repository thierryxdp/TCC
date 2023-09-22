def inverte(frase):
   s=str.split(frase," ")
   s.reverse()
   str.join("",s)
   L=[".",",","!","?","-","...",";",":"]
    for c in L:    
    	frase=str.replace(frase,c," ")
    return frase
	
   return str.join("",s)