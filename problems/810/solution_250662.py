def inverte(frase):
   frase=retira_pontuacao(frase)
   frase=str.split(frase," ")
   frase.reverse()
   frase=str.join(" ",frase[1:])	
   frase=str.lower(frase)
   return frase

def retira_pontuacao(frase):
    L=[".",",","!","?","-","...",";",":"]
    for c in L:    
    	frase=str.replace(frase,c," ")
    return frase