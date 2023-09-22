def retira_pontuação (frase):
    frase = str.replace(frase, "?", " ")
    frase = str.replace(frase, "!", " ")
    frase = str.replace(frase, ":", " ")
    frase = str.replace(frase, ";", " ")
    frase = str.replace(frase, ".", " ")
    frase = str.replace(frase, "...", " ")
    frase = str.replace(frase, "-", " ")
    frase = str.replace(frase, ",", " ")
    return frase

def inverte(frase):
    frase = retira_pontuação(frase)
    frase = frase.split(" ")
    frase.reverse()
    frase = ' '.join(frase)
    return frase