def retira_pontuacao(frase):
    frase = frase
    for n in [".", "!", ":", ";", "-", ","]:
        frase = frase.replace(n, " ")
    return frase