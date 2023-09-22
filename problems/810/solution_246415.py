def retira_pontuacao(frase):
    frase=str.replace(frase, ".", " ")
    frase=str.replace(frase, "...", " ")
    frase=str.replace(frase, "-", " ")
    frase=str.replace(frase, ";", " ")
    frase=str.replace(frase, "!", " ")
    frase=str.replace(frase, ":", " ")
    frase=str.replace(frase, "?", " ")
	frase=str.replace(frase, ",", " ")
    return frase

 def inverte(frase):
        
     retira_pontuacao(frase.(reverse=True))
     return frase