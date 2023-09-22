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
    a=len(texto)
    texto=texto.reverse()
    return "".join(texto)