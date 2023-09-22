def retira_pontuacao1(frase):
    frase = frase.replace("!","/")
    frase = frase.replace("?","/")
    frase = frase.replace("...","/")
    frase = frase.replace(".","/")
    frase = frase.replace(":","/")
    frase = frase.replace(",","/")
    frase = frase.replace(";","/")
    frase = frase.replace("-","/")
    frase = frase.split("/")
    frase = " ".join(frase)
    return frase

def inverte(frase):
    frase = retira_pontuacao1(frase)
    frase = str.lower(frase)
    frase = frase.split()
    frase = frase[::-1]
    frase = " ".join(frase)
    return frase