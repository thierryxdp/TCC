def inverte(frase):
   s=str.split(frase," ")
   s.reverse()
   str.join("",s)
  
	
   return str.join("",s)

def retira_pontuacao(frase):
    L=[".",",","!","?","-","...",";",":"]
    for c in L:    
    	frase=str.replace(frase,c," ")
    return frase