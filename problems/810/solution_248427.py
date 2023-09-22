def inverte(frase):
    frase = frase.lower()
    frase = retira_pontuacao(frase)
    frase = frase.split(" ")
    frase = frase[::-1]
    frase = ' '.join(frase)
    return frase