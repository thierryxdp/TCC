def retita_pontuacao(frase):
    frase=frase.replace("-"," ")
    frase=frase.replace("!"," ")
    frase=frase.replace(","," ")
    frase=frase.replace("."," ")
    frase=frase.replace("?"," ")
    frase=frase.replace(":"," ")
    frase=frase.replace(";"," ")
    return frase

def inverte(frase):
    frase=frase.lower()
    frase=retira_pontuacao(frase)
    frase=frase.split(" ")
    frase=[::-1]
    frase=" ".join(frase)
    return frase