def retira_pontuacao (frase):
    frase = str.split(frase, ".")
    frase2 = str.join(frase, " ")
    frase2 = str.split(frase, ",")
    frase3 = str.join(frase, " ")
    frase3 = str.split(frase, ";")
    frase4 = str.join(frase, " ")
    frase4 = str.split(frase, ":")
    frase5 = str.join(frase, " ")
    frase5 = str.split(frase, "!")
    frase6 = str.join(frase, " ")
    frase6 = str.split(frase, "?")
    frase7 = str.join(frase, " ")
    return frase7