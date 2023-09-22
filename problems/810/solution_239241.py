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
    texto=str.split(texto)
    return "".join(reversed(texto))