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

def inverte(retira_pontuacao(frase)):
    frase1 = frase.split()
    return frase1