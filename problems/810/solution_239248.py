def retira_pontuacao(texto):
    texto=texto.replace("!"," ")
    texto=texto.replace("?"," ")
    texto=texto.replace(";"," ")
    texto=texto.replace(":"," ")
    texto=texto.replace("."," ")
    texto=texto.replace("..."," ")
    texto=texto.replace(","," ")
    texto=texto.replace("-"," ")
    return texto
def inverte(texto):
    texto=retira_pontuacao(texto)
    texto=texto.split(" ")
    texto=texto[-1::-1]
    texto=str.join(" ",texto)
    texto=str.lower(texto)
    texto=str.strip(texto)
    return texto