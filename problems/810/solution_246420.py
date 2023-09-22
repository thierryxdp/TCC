def retira_pontuacao(frase):
    frase=str.replace(frase, ".", " ")
    frase=str.replace(frase, "...", " ")
    frase=str.replace(frase, "-", " ")
    frase=str.replace(frase, ";", " ")
    frase=str.replace(frase, "!", " ")
    frase=str.replace(frase, ":", " ")
    frase=str.replace(frase, "?", " ")
	frase=str.replace(frase, ",", " ")

def inverte(frase):
    retira_pontuacao(frase)
    frase = frase.reverse()
    return frase