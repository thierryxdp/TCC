def inverte(frase):
   s=str.split(frase," ")
	return s.reverse + retira_pontuacao(frase)
def retira_pontuacao(frase):
    L=[".",",","!","?","-","...",";",":"]
    for c in L:    
    	frase=str.replace(frase,c," ")
    return frase