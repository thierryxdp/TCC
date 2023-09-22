def retira_pontuacao(frase):
    frase = str.replace(frase,"-"," ")
    frase = str.replace(frase,","," ")
    frase = str.replace(frase,":"," ")
    frase = str.replace(frase,";"," ")
    frase = str.replace(frase,"..."," ")
    frase = str.replace(frase,"!"," ")
    frase = str.replace(frase,"?"," ")
    return str.replace(frase,"."," ")

def inverte(frase):
	frase = retira_pontuacao(frase)
	return str.join(" ",str.split(frase," "),-1)