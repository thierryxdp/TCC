def retira_pontuacao(frase):
    frase = frase.replace("!","/")
    frase = frase.replace("?","/")
    frase = frase.replace("...","/")
    frase = frase.replace(".","/")
    frase = frase.replace(":","/")
    frase = frase.replace(",","/")
    frase = frase.replace(";","/")
    frase = frase.split("/")
    frase = " ".join(frase)
    return frase