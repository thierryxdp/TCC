#Essa função retira a pontuação pedida tal como vírgulas, travessão, etc.

def retira_pontuacao(frase):
    frase = str.split(frase, "!")
    frase = str.join(" ", frase)
    frase = str.split(frase, ",")
    frase = str.join(" ", frase)
    frase = str.split(frase, ".")
    frase = str.join(" ", frase)
    frase = str.split(frase, "-")
    frase = str.join(" ", frase)
    frase = str.split(frase, "?")
    frase = str.join(" ", frase)
    return frase