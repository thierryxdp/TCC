def retira_pontuacao(frase):

    frase = str.replace(frase, "-", "", 1000)
    frase = str.replace(frase, ",", "", 1000)
    frase = str.replace(frase, ":", "", 1000)
    frase = str.replace(frase, ";", "", 1000)
    frase = str.replace(frase, ".", "", 1000)
    frase = str.replace(frase, "!", "", 1000)
    frase = str.replace(frase, "?", "", 1000)

    return frase