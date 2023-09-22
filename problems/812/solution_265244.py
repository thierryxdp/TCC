def retira_pontuacao(frase):
    if ":" in frase:
        frase = frase.replace(":", " ")
        frase = frase.replace(";", " ")
        frase = frase.replace(".", " ")
        frase = frase.replace("!", " ")
        frase = frase.replace("-", " ")
        frase = frase.replace(",", " ")
        frase = frase.replace("?", " ")
        return frase