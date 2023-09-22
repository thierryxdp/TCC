#4
def inverte(texto):
    texto=texto.lower()
    texto=texto.replace("-"," ")
    texto=texto.replace(",", " ")
    texto=texto.replace(":"," ")
    texto=texto.replace(";"," ")
    texto=texto.replace("."," ")
    texto=texto.replace("!"," ")   
    texto=texto.replace("?"," ")
    texto=texto.replace("..."," ")
    texto=texto.split()
    texto.reverse()
    texto=tuple(texto)
    texto=str.join(" ",texto)
    return texto