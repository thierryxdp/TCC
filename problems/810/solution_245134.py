def inverte (frase):
    frase = frase.split()
    frase = list(reversed(frase))
    retira_pontuacao()
    return (" ".join(frase))