def retira_pontuacao(frase):
    frase=frase.replace("."," ")
    frase=frase.replace(";"," ")
    frase=frase.replace("!"," ")
    frase=frase.replace("?"," ")
    frase=frase.replace("..."," ")
    frase=frase.replace("-"," ")
    frase=frase.replace(":"," ")
    return frase
def inverte(frase):
    frase=retira_pontuacao
    str.lower(frase)
    aux=frase.split()
    aux[::-1]
    frase=str.join(' ',aux)
    return frase