def retira_pontuacao(frase):
    frase = str.split(frase, ".") and str.split(frase, ",") and str.split(frase, ";") and str.split(frase, ":") and str.split(frase, "!") and str.split(frase, "?")
    frase = str.join(" ", frase)
    return frase