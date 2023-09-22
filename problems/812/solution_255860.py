def retira_pontuação(frase):
    frase = str.split(frase, "/" "," ":" ".")
    frase = str.join(" ", frase)
    return frase