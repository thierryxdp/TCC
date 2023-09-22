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
	frase = frase[::-1]
	return str.lower(frase)