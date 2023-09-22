def retira_pontuacao(frase):
    frase=frase.replace("-"," ")
    frase=frase.replace(","," ")
    frase=frase.replace(":"," ")
    frase=frase.replace(";"," ")
    frase=frase.replace("."," ")
    frase=frase.replace("!"," ")
    frase=frase.replace("?"," ")
    return frase

def inverte(frase):
    a=retira_pontuacao(frase)
    b=a.lower()
    lista=b.split()
    lista2=lista[::-1]
    return lista2.join()