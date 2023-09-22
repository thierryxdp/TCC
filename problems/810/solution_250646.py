def inverte(frase):
   frase=retira_pontuacao(frase)
   frase=str.split(frase," ")
   frase.reverse()
   str.join("",frase)	
   return str.join("",frase)

def retira_pontuacao(frase):
    L=[".",",","!","?","-","...",";",":"]
    for c in L:    
    	frase=str.replace(frase,c," ")
    return frase