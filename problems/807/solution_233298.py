def conta_frases(texto):
    texto.replace("...","#")
    texto.replace(".","#")
    texto.replace("?","#")
    texto.replace("!","#")
    lista=texto.split("#")
    return len(lista)