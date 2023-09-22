def retira_pontuacao(frase):
    frase = frase.replace(".", " ")
    frase = frase.replace("-", " ")
    frase = frase.replace(":", " ")
    frase = frase.replace(";", " ")
    frase = frase.replace(".", " ")
    frase = frase.replace("?", " ")
    frase = frase.replace("!", " ")
    frase = frase.replace(",", " ")
	return frase

def inverte(frase):
    frase = retira_pontuacao(frase)
    frase = frase.split()
    frase = frase.reverse()
    return frase