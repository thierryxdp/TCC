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
    return "".join(reversed(texto))