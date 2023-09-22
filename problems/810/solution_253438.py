def retira_pontuacao(frase):
    frase=frase.replace("-"," ")
    frase=frase.replace("!"," ")
    frase=frase.replace(","," ")
    frase=frase.replace("."," ")
    frase=frase.replace("?"," ")
    frase=frase.replace(":"," ")
    frase=frase.replace(";"," ")
    return frase

def inverte(x):
    x=x.lower()
    x=retira_pontuacao(x)
    x=x.split(" ")
    x=" ".join(x)
    return x