def inverte(frase):
   frase=retira_pontuacao(frase)
   frase=str.split(frase," ")
   s.reverse()
   str.join("",s)	
   return str.join("",s)

def retira_pontuacao(frase):
    L=[".",",","!","?","-","...",";",":"]
    for c in L:    
    	frase=str.replace(frase,c," ")
    return frase