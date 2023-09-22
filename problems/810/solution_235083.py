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
	frase = str.split(frase," ")
	frase = frase[::-1]
	frase = str.join(" ",frase)
    frase = str.replace(frase, "  "," ")
	return str.lower(str.strip(frase))