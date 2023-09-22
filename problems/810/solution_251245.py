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
    frase1 = frase.split()
    frase = ' '.join(frase1)
    return frase