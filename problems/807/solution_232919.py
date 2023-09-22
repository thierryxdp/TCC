def conta_frases(frase):
    frase = retira_pontuacao(frase)
    frase = str.split(frase, '.')
    frase = len(frase)
    return frase - 1