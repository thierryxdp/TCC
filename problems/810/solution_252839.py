def inverte(frase):

    frase = retira_pontuacao(frase)
    frase = frase.lower()
    frase = frase.split()
    frase.reverse()
    frase = " ".join(frase)
    return(frase)
def retira_pontuacao(frase):
    if "." in frase:
        frase = frase.replace("."," ")
    if "!" in frase:
        frase = frase.replace("!"," ")
    if "?" in frase:
        frase = frase.replace("?"," ")
    if "..." in frase:
        frase = frase.replace("..."," ")
    if "," in frase:
        frase = frase.replace(","," ")
    if "-" in frase:
        frase = frase.replace("-"," ")
    return rase